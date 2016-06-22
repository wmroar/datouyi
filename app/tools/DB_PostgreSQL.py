#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import itertools
import psycopg2
import os
import sqlalchemy.pool as pool
import threading


# 解决 pg TypeError: Decimal('30737') is not JSON serializable， 的bug
DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)


# from libs import helper

class Connection(object):

    """
    #host 数据库主机
    #database 数据库名称
    #user 数据库名称
    #password 数据库连接密码
    """

    def __init__(self, host, database, user, password, debug=False):
        """
        #ORACEL UTF-8 WINDOW XP 很操蛋
        """
        if 'NLS_LANG' not in os.environ or os.environ["NLS_LANG"] != 'AMERICAN_AMERICA.AL32UTF8':
            os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"

        self.host = host
        self.database = database
        # 用于判断是否打印sql
        self.debug = debug

        args = {'database': database}
        if user is not None:
            args['user'] = user
        if password is not None:
            args['password'] = password

        pair = host.split(':')
        if len(pair) == 2:
            args['host'] = pair[0]
            args['port'] = int(pair[1])
        else:
            args['host'] = pair[0]
            args['port'] = 1521

        self.args = args
        self._db = None
        # 单位为秒
        self._db_operation_timeout = 300

        # 连接池
        self.conn_pool = pool.manage(
            psycopg2, pool_size=20, max_overflow=40, timeout=self._db_operation_timeout, recycle=1800)

        self.reconnection()

    #-----------------------------内部函数-------------------------------
    def _ensure_connected(self):
        if self._db:
            self._db.close()

        self.reconnection()

    def _cursor(self):
        self._ensure_connected()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters):
        t = threading.Timer(self._db_operation_timeout, self.cancel)
        t.start()

        self._log_sql("sql: %s" % str(query))
        self._log_sql("param: %s" % str(parameters))

        try:
            cursor.execute(query, parameters)
            self.commit()
        except psycopg2.DatabaseError as e:
            self._db.rollback()

            raise Exception(
                """errr_info:%s \n           sql: %s""" % (str(e), query) )
        finally:
            t.cancel()

    def _executemany(self, cursor, query, parameters):
        t = threading.Timer(self._db_operation_timeout, self.cancel)
        t.start()

        self._log_sql(query)
        self._log_sql("param: %s" % str(parameters))

        try:
            cursor.executemany(query, parameters)
            self.commit()
        except  psycopg2.IntegrityError as e:
            self._db.rollback()
            raise e
        except psycopg2.DatabaseError as e:
            self._db.rollback()
            raise Exception(
                """errr_info:%s \n           sql: %s""" % (str(e), query) )
        finally:
            t.cancel()

    #-----------------------------内部函数-------------------------------

    def sure_alive(self):
        """确保连接正常
        """
        try:
            self._db.ping()
        except Exception, e:
            self.reconnection()

    def reconnection(self):
        self._db = None
        # 利用连接池,如果连接池存在会从连接池取连接，只有当没有连接的时候才会去重新连接
        self._db = self.conn_pool.connect(host=self.args['host'],
                                          database=self.args['database'],
                                          user=self.args['user'],
                                          password=self.args['password'],
                                          port=self.args['port'])

    def close(self):
        if getattr(self, "_db", None) is not None:
            try:
                self._db.close()
            except Exception, e:
                print e
            self._db = None

    def commit(self):
        if getattr(self, "_db", None) is not None:

            t = threading.Timer(self._db_operation_timeout, self.cancel)
            t.start()

            self._db.commit()

            t.cancel()

    def rollback(self):
        if getattr(self, "_db", None) is not None:

            t = threading.Timer(self._db_operation_timeout, self.cancel)
            t.start()

            self._db.rollback()

            t.cancel()

    def cancel(self):
        if getattr(self, "_db", None) is not None:
            try:
                self._db.cancel()
            except Exception, e:
                print 'info:user requested cancel of current operation'

    def __del__(self):
        self.close()

    def _log_sql(self, sql):
        """将sql语句写入日志 -将生成的sql记录在 log_sql.txt 中,一般在query(sql)的前面调用本函数
        @param sql(str):sql语句
        """
        if self.debug:
            try:
                f = open(
                    os.path.dirname(os.path.realpath(__file__)) + '/pg_log_sql.txt', 'a+')
                print >> f, sql
                f.close()
            except:
                pass

    #-------------------------------查询------------------------------
    """
    users = db.query("select * from user where uid >= :uid", 5)
    for user in users:
        print user.uid, user.name
    """

    def query(self, query, parameters=tuple()):
        cursor = self._cursor()

        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            query_datas = [Row(itertools.izip(column_names, row))
                           for row in cursor]
            return query_datas
        finally:
            cursor.close()

    # 获取数据并且返回数据头
    def query_with_titles(self, query, parameters=tuple()):
        cursor = self._cursor()

        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            query_datas = [Row(itertools.izip(column_names, row))
                           for row in cursor]
            return query_datas, column_names
        finally:
            cursor.close()

    # 获取数据为列表,不返回字典
    def simple_query(self, query, parameters=tuple()):
        cursor = self._cursor()

        try:
            self._execute(cursor, query, parameters)
            query_datas = [row for row in cursor]
            return query_datas
        finally:
            cursor.close()

    def get(self, query, parameters=tuple()):
        """
        #单次查询,返回单行较有用，比如
        user = db.get("select * from user where uid = :uid", 5)
        print user.uid, user.name
        """
        rows = self.query(query, parameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    # ITER QUERY
    def iter(self, query, parameters=tuple()):
        """
        #迭代查询,使用yield生成器。查询返回多行，结果集数据量较大的时候较有用
        for user in db.iter("select * from user where uid >= :uid", 5):
            print user.uid, user.name
        """
        cursor = self._cursor()

        self._execute(cursor, query, parameters)
        column_names = [d[0] for d in cursor.description]
        return self._iter_qrow(cursor, column_names)

    def _iter_qrow(self, cursor, column_names):
        for row in cursor:
            yield Row(itertools.izip(column_names, row))
        cursor.close()

    #-------------------------------执行---------------------------------
    def execute(self, query, parameters=tuple()):
        """
        执行一条sql，比如update, insert, delete等操作。查询select请使用 query，get, iter
        last_row_id = db.execute("update user set name = ':name' where uid = :uid", "boyaa", 5)
        print last_row_id
        """
        return self.execute_lastrowid(query, parameters)

    def execute_lastrowid(self, query, parameters=tuple()):
        """
        执行一条 sql, 同上,execute()是execute_lastrowid
        """
        cursor = self._cursor()

        try:
            self._execute(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def execute_rowcount(self, query, parameters=tuple()):
        """
        #执行一条sql，与execute_lastrowid（）功能一样，只不过返回的是rowcount
        """
        cursor = self._cursor()

        try:
            self._execute(cursor, query, parameters)
            return cursor.rowcount
        finally:
            cursor.close()

    #-------------------------------执行---------------------------------

    """
    #执行多条语句
    sql = "insert into user (uid, name) values (%(uid)s, %(name)s)"
    data_2 = [{'uid':5, 'name':'boyaa_1'}, {'uid':6, 'name':'boyaa_2}]
    executemany(sql, data_2)
    """

    def executemany(self, query, parameters):
        return self.executemany_lastrowid(query, parameters)

    def executemany_lastrowid(self, query, parameters):
        cursor = self._cursor()

        try:
            self._executemany(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def executemany_rowcount(self, query, parameters):
        cursor = self._cursor()

        try:
            self._executemany(cursor, query, parameters)
            return cursor.rowcount
        finally:
            cursor.close()

    #//
    def execute_callproc(self, call_proc_name, date):
        cursor = self._cursor()
        try:
            cursor.callproc(call_proc_name, date)
        except Exception, e:
            raise e
        finally:
            cursor.close()


class Row(dict):

    """访问对象那样访问dict,行结果"""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


if __name__ == "__main__":
    import sys
    import flask
    from tornado.escape import _unicode
    import os

    os.environ['NLS_LANG'] = "SIMPLIFIED_CHINESE_CHINA.UTF-8"

    # old
    db_host = "175.45.5.236:5432"
    db_name = "boyaadw"

    db_user = "analysis"  # "stage"
    db_pswd = "analysis"  # "stage"

    db = Connection(db_host, db_name, db_user, db_pswd)

    for game in db.query("select fname from game_dim where fisgame = 1 and rownum = 1"):
        print game.FNAME

    sql = "insert into tmp_zhoupeng_123(fid, fname) values(:id, :name)"
    parameters = [{'id': 123, 'name': 'wewewe'}, {'id': 345, 'name': 'rrrr'}]
    print db.executemany_rowcount(sql, parameters)

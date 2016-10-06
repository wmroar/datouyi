# -*- coding: utf-8 -*-
"""
    byl_mobile
    ~~~~~~

    数据中心核心数据展示系统

    :copyright: (c) 2014 by 数据中心.
"""

from flask import session, g, request, current_app
# import redis
import os
#from libs.DB_Mysql import Connection
import platform
from views.comview import comm
from views.product import pro
import datetime
import urllib
# blue modules
BLUE_MODULE_LIST = [comm,pro]





def bootstrap(app):
    # 设置时区
    os.environ["TZ"] = "GMT-08"

    # add blueprint module
    for module in BLUE_MODULE_LIST:
        app.register_blueprint(module)

    def _get_db():
        pg_db = Connection(app.config['DB_HOST'],
                           app.config['DB_NAME'],
                           app.config['DB_USER'],
                           app.config['DB_PSWD'],
                           app.config['DEBUG'])

        return pg_db

    # def _get_redis_db():
    #     redis_db = None
    #     redis_list = []
    #     for db_index in range(32):
    #         pool = redis.ConnectionPool(host=app.config['REDIS_HOST'],
    #                                     port=app.config['REDIS_PORT'],
    #                                     db=db_index)

    #         tmp_db = redis.Redis(connection_pool=pool)
    #         redis_list.append(tmp_db)

    #         if db_index == 0:
    #             redis_db = tmp_db

    #     return redis_db, redis_list

    # def _get_mongo_db():
    #     mongo_db =  MongoClient(app.config['MONGO_URI'])
    #     if not app.config['DEBUG']:
    #         mongo_db.dcnew.authenticate("dcuser","om9lk5sokdhXfilrKvb")
    #     return mongo_db.dcnew


    """这里是暂时取消了
    """
    pg_db = _get_db()
    # redis_db, redis_list = _get_redis_db()
    # mongo_db = _get_mongo_db()

    # # 连接impala
    # impalaConn = None
    # if platform.system() == 'Linux':
    #     impalaConn = ImpalaSql()



    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = datetime.timedelta(minutes=60*12)

    @app.before_request
    def get_db():
        pass
        g.db = pg_db
        # g.impala_db = impalaConn
        # g.redis_db = redis_db
        # g.redis_list = redis_list
        # g.mongo_db = mongo_db

    # 从session中获取gpv
    # 没有获取到默认取所有权限

        # g.gpv = ['1396895|58930167|58930180']

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Credentials, Methods")
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')

        return response

# -*- coding:utf-8 -*-

from sql_template import  KIND_TPL
import logging

class BaseEntity(object):

    def __init__(self):
        self.db = None

    def update(self):
         pass

    def query(self,condition):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def execute(self,sql):
        logging.warning(sql)
        datas = self.db.query(sql)
        return {'datas': datas}

    def gen_condition(self):
        result = ''
        for key,value in self.args.items():
            result += ' and ' + key + ' = ' + str(value)
        return result


class Kind(BaseEntity):
    def __init__(self,db,args):
        self.db = db
        self.sql = KIND_TPL.get('recure_tpl')
        self.args = args

    def get_all(self):
        sql_dict = {'condition':''}
        return self.execute(self.sql % sql_dict)

    def get_by_level(self):
        sql_dict = {'condition':self.gen_condition()}
        return self.execute(self.sql % sql_dict)
    
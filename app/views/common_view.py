# -*- coding:utf-8 -*-
from tornado.web import RequestHandler
from models.entity import Kind
import logging

class BaseHandler(RequestHandler):

    def initialize(self,database):
        self.db = database


class KindHandler(BaseHandler):

    def get(self):
        sql_dict = {
            'level' : int(self.get_argument('level',0)) + 1
        }
        kind = Kind(self.db,sql_dict)
        type = self.get_argument('all','0')
        if type == '1':
            self.write(kind.get_all())
            return
        else:
            self.write(kind.get_by_level())


    def post(self):

        sql_dict = {
            'id':self.get_argument('id',None),
            'name':self.get_argument('name',None),
            'des' : self.get_argument('des',None),
        }

        type = self.get_argument('type','update')
        kind = Kind(self.db,sql_dict)

        if type == 'update':
            pass


# -*- coding:utf-8 -*-
from tornado.web import Application
from config import settings
from tornado.options import define,parse_config_file,options
from views.url_list import handlers
from tools.DB_PostgreSQL import  Connection
from tornado.ioloop import IOLoop
import logging

import os
import config
import sys


#增加内部接口访问路径
cur_path = os.path.dirname(__file__)
sys.path.append(cur_path)

class ApplicationImpl(Application):

    def __init__(self):

        self._set_config()
        self.db = Connection( config.DB_HOST, config.DB_NAME,
                              config.DB_USER, config.DB_PSWD, settings.get('debug'))
        #重写参数
        ehandlers = [ x + (dict(database = self.db),) for x in handlers]

        Application.__init__(self,handlers = ehandlers,default_host='localhsot',transforms=None,**settings)


    def _set_config(self):
        custom_keys = ['font_dir', 'app_host', 'app_port', 'DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PWSD',
                        'auth_login_url', 'auth_trader_login_url', 'auth_login_domain', 'log_path', 'admin_emails']

        for key in custom_keys:
            if key == 'admin_emails':
                define(key,type=list)
            else:
                define(key)

        parse_config_file(os.path.join(cur_path,'config.py'),final=False)


app = ApplicationImpl()
print 'starting listen'
app.listen(9999)

IOLoop.instance().start()
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=options.log_path,
                    filemode='a')
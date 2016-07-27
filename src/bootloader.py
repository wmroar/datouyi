#!/usr/bin/env python
#coding=utf8

import os
from jinja2 import Environment, FileSystemLoader
from jinja2 import MemcachedBytecodeCache
import setting
from lib.util import setting_from_object
from lib.database import Db
from lib import uimodules
import redis

settings = setting_from_object(setting)

settings.update({
        'template_path':os.path.join(os.path.dirname(__file__), 'template'),
        'static_path':os.path.join(os.path.dirname(__file__), 'style'),
        'upload_path':os.path.join(os.path.dirname(__file__), 'upload'),
        'cookie_secret':"55c66d9b67ce4553996824ed16aa74d1=",
        'login_url':'/signin',
        "xsrf_cookies": True,
        'ui_modules' : uimodules,
        'autoescape':None,
        'session_secret' : "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
        'session_timeout' : 3600,
        'redis_host' : 'localhost',
        'redis_port' : 4500,
        'redis_pass' : '',
    })


bcc = None
if settings['debug'] == False:
    bcc = MemcachedBytecodeCache(memcachedb)

jinja_environment = Environment(
            loader = FileSystemLoader(settings['template_path']),
            bytecode_cache = bcc,
            auto_reload = settings['debug'],
            autoescape = False)

db = Db({'db':settings['db_name'], 'host':settings['db_host'], 'port':settings['db_port'], \
               'user':settings['db_user'], 'passwd':settings['db_passwd'], 'charset':'utf8'})


redis_db = redis.StrictRedis(host=settings['redis_host'], port=settings['redis_port'], password=settings['redis_pass'])


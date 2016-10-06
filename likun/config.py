# -*- coding: utf-8 -*-
from datetime import timedelta

"""
run host and port
"""
APP_HOST = '127.0.0.1'
APP_PORT = 9999


"""
config attribute
"""
DEBUG = True
DEBUGER = 1622


"""
PG Database Configuration
"""
DB_HOST = "localhost:3306"
DB_NAME = "likun"
DB_USER = "root"  # "stage"
DB_PSWD = "wang@2016__"  # "stage"

"""
REDIS Database Configuration
"""
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 4500
REDIS_DB = 0
# 缓存多少天的数据
REDIS_CACHE_DAYS = 32
# IS_CACHE = False
IS_CACHE = False


"""
session seting
"""
SESSION_COOKIE_NAME = 'mobile_session'
SECRET_KEY = r'%9phlwUzctY^1!pz'
PERMANENT_SESSION_LIFETIME = timedelta(days=1)



"""
login url
"""


"""
Mail seting
"""
ADMINS_MAIL_LIST = ['wang_303496@163.com', ]
MAIL_HOST = 'mail.163.com'
MAIL_PORT = '587'
MAIL_FROMADDR = 'noreply@boyaa.com'
MAIL_USERNAME = 'noreply'
MAIL_PASSWORD = 'noReply#boyaa'

"""
Logging File
"""
LOGGING_FILE = 'tmp\\likun_app.log'

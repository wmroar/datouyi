# -*- coding:utf-8 -*-

settings = {
    'debug' : True,

    'xsrf_cookies' : False,

    # 设置cookie密钥：
    'cookie_secret' : "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",

    'login_url' : "/login",

    # 设置静态文件解析路径：
    'static_path'   : "/fuck/",
    # 'static_path'   : os.path.join(CURRENT_PATH, "static"),

    #设置静态路径头部：
    # 'static_url_prefix' : "/static/",
    'static_url_prefix' : "http://d.boyaa.com/",

    # 设置静态文件处理类：
    # static_handler_class : MyStaticFileHandler,
}

app_host = 'localhost'

app_port = '9999'


DB_HOST = 'localhost:5432'
DB_NAME = ''
DB_USER = 'postgres'
DB_PSWD = 'wang123'

log_path = 'thislog.log'
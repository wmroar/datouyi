# -*- coding: utf-8 -*-
"""
    byl_core.factory
        ~~~~~~~~~~~~~~~~

    byl_core factory module
"""

import os

from flask import Flask
from flask.sessions import SecureCookieSessionInterface
#from flask.ext.compress import Compress

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


def add_file_handler(app):
    file_handler = RotatingFileHandler(app.config['LOGGING_FILE'],
                                       maxBytes=1024 * 1024 * 100,
                                       backupCount=20,
                                       delay=False)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(file_handler)


def add_mail_handler(app):
    mail_handler = SMTPHandler(mailhost=(app.config['MAIL_HOST'], app.config['MAIL_PORT']),
                               fromaddr = app.config['MAIL_FROMADDR'],
                               toaddrs = app.config['ADMINS_MAIL_LIST'],
                               subject = 'Server error',
                               credentials = (
        app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']),
        secure = ()
    )

    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter('''
                                        Message type:       %(levelname)s
                                        Location:           %(pathname)s:%(lineno)d
                                        Module:             %(module)s
                                        Function:           %(funcName)s
                                        Time:               %(asctime)s

                                        Message:

                                        %(message)s
                                        '''))

    app.logger.addHandler(mail_handler)


def add_logger_handler(app):
    # add logging handler
    if not app.debug:
        # 设置logger告警级别默认 warning级别
        app.logger.setLevel(logging.WARNING)

        add_file_handler(app)

        if app.config.get('MAIL_HOST', None):
            # add error send mail function
            add_mail_handler(app)


def create_app(package_name, config_filename, **kwargs):
    app = Flask(package_name, **kwargs)

    app.config.from_pyfile(config_filename)

    app.session_interface = SecureCookieSessionInterface()
    app.session_interface.key_derivation = None

    # 添加错误日志处理模块
    add_logger_handler(app)

    # 将后端返回的json数据进行压缩减少传输
    #Compress(app)

    return app





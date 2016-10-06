# -*- coding: utf-8 -*-
"""
    byl_mobile
    ~~~~~~

    数据中心核心数据展示系统

    :copyright: (c) 2014 by 数据中心.
"""

import os
import datetime
import re
import flask
from flask import Flask, request, session, g, Response, Blueprint, current_app,url_for,render_template
from werkzeug import secure_filename
import json

# from libs.models import *


pro = Blueprint('pro', __name__, url_prefix='/pro')


##################################

@pro.route('/addpro/',methods = ['post'])
def do_add_pro():
    current_app.logger.info(request.form)
    args = request.form
    pro_section = args.get('prosection',1)
    pro_name = args.get('proname')
    pro_title = args.get('protitle')
    pro_price = args.get('proprice')
    current_app.logger.info(dir(request))
    pro_pic = args.get('propic')
    pro_content = args.get('editorValue')
    pro_prioriry = int(args.get('proprioriry',0))
    pro_source = args.get('prosource','unkonwn')
    f = request.files['propic']
    path = os.path.join(current_app.static_folder, 'uploadpic')
    secure_f = secure_filename(f.filename)
    file_path = os.path.join(path,secure_f)
    f.save(file_path)
    url_file_path = url_for('static',filename ='uploadpic/' + secure_f,_external=True)

    sql_dict = {
        'title': pro_title,
        'name': pro_name,
        'content': pro_content,
        'user_id': 0,
        'prioriry': pro_prioriry,
        'price': pro_price,
        'source': pro_source,
        'major_pic':url_file_path,
        'section_id':pro_section
    }


    sql = """insert into product(section_id,title,name,content,user_id,prioriry,price,source,major_pic)
             values 
             (%(section_id)s,%(title)s,%(name)s,%(content)s,
              %(user_id)s,%(prioriry)s,%(price)s,%(source)s,%(major_pic)s)
    """
    g.db.execute(sql,sql_dict)
    return '添加成功'

@pro.route('/detail/')
def index_pro_detail():
    id = request.args.get('id',0)
    sql = "select title,read_num,content from product where id = %(id)s"
    data = g.db.query(sql,{'id':id})
    return render_template('prodetail.html',data=data)

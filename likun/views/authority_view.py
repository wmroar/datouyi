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
from flask import Flask, request, session, g, Response, Blueprint, current_app
import json

# from libs.models import *
from dc_business_support.common import auth

from dc_query_pg.common import public_func

from dc_business_support.control import authority_control
from dc_business_support.common.dims_new import dimChinese, get_sql_flag
from common_view import find_and_instantiate_class
from libs import helper
from libs import SendEmail
from libs import warning_way
from libs.helper import get_handle_result_code

authority = Blueprint('authority', __name__, url_prefix='/new/authority')


##################################
@authority.route("/list/")
@auth.gpv_required2
def authority_list():

    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["fuid"] = args.get('fuid', 0)
    args["status"] = args.get('status', 1)
    if not args["fuid"]:
        args["table_format"] = "authlist_1"
    else:
        args["table_format"] = "authlist_other"
    result = authority_control.get_authority(args)
    return flask.jsonify(result)


@authority.route("/apply/list/")
@auth.gpv_required2
def apply_list():
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["status"] = args.get('status', 0)
    args["table_format"] = "apply_%s" % args["status"]
    result = authority_control.get_apply(args)
    return flask.jsonify(result)


@authority.route("/apply/cancel/", methods=['GET', 'POST'])
@auth.gpv_required2
def apply_cancel():
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["id"] = args.get('id', 0)
    if not args["id"]:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'参数错误！'))
    if authority_control.cancel_apply(args):
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.SUCCESS, u'删除成功！'))
    else:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'删除失败！'))


@authority.route("/game/filter/list/")
@auth.gpv_required2
def game_filter_list():
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    return flask.jsonify(authority_control.game_filter_list())


@authority.route("/game/terminal/filter/list/")
@auth.gpv_required2
def game_terminal_filter_list():
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["game_id"] = args.get("game_id",0)
    if args["game_id"]:
        return flask.jsonify(authority_control.games_filter_list_info_terminal(args["game_id"]))


@authority.route("/game/langtype/filter/list/")
@auth.gpv_required2
def game_langtype_filter_list():
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["game_id"] = args.get("game_id",0)
    args["terminal_id"] = args.get("terminal_id",0)
    if args["game_id"]:
        return flask.jsonify(authority_control.games_filter_list_info_langtype(args["game_id"],args["terminal_id"]))


@authority.route("/gameinfo/")
@auth.gpv_required2
def gameinfo():
    """ 获取筛选条件 加载列表
    """
    args = public_func.get_all_args(request.args, request.form)
    args["game_id"] = args.get("game_id",0)
    args["terminal_id"] = args.get("terminal_id",0)
    args["langtype_id"] = args.get("langtype_id",0)
    args["table_format"] = "gameinfo"
    if not args['game_id']:
        return flask.jsonify({'error_message':'缺失游戏ID', 'error_code': 2})

    result = authority_control.authority_get_gameinfo_new3(args,args['game_id'], args["terminal_id"], args["langtype_id"])

    return flask.jsonify(result)


@authority.route("/apply/", methods=['POST', 'GET'])
@auth.gpv_required2
def apply_application():
    """ 申请游戏平台版本
    """
    args = public_func.get_all_args(request.args, request.form)
    infolist  = args.get('infolist','')
    reasons   = args.get('reasons', '')
    fuid = int(args.get('fuid', 0))
    infolist = infolist.split(",")

    if not len(infolist):
        return flask.jsonify( {'error_code':1000,'error_message':'空游戏应用或者空申请理由!'} )
    if not fuid and not reasons:
        return flask.jsonify( {'error_code':1000,'error_message':'空游戏应用或者空申请理由!'} )

    deallist  = [info.split("|")[5] for info in infolist]  #获得审批人，发邮件通知

    if fuid:
        result = authority_control.pers_distribute(infolist, fuid)
    else:
        result = authority_control.apply_application(infolist, reasons)
    if result:
        # 申请成功, 进入审批阶段, 邮件告诉初级审批人
        if deallist and not fuid:
            mail_messages = '你有待审批的游戏应用, 请及时审批. <a href="http://data.oa.com/dc_new/#/authority/approvelist"> http://data.oa.com/dc_new/#/authority/approvelist </a>'
            sendEmailExt( getNameList( deallist ), mail_messages )

        return flask.jsonify(get_handle_result_code(helper.ErrorCode.SUCCESS,u'操作成功！'))
    else:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR,u'操作错误，请联系管理员！'))


@authority.route("/approving/")
@auth.gpv_required2
def authority_get_approving():
    """ 审批人：待审批，已审批，驳回
    """

    args = public_func.get_all_args(request.args, request.form)
    args["status"] = args.get("status",'not')

    args["table_format"] = "approving_%s" % args["status"]
    result = ''
    # 待审批
    if args["status"] == 'not':
        result = authority_control.authority_get_approving_not_new(args)
    # 已审批
    elif args["status"] == 'yet':
        result = authority_control.authority_get_approving_yet(args)
    # 驳回
    elif args["status"] == 'rebut':
        result = authority_control.authority_get_approving_rebut(args)

    # # 兼容前端大小写问题
    # if status == 'not':
    #     rows = []
    #     for row in result['data']:
    #         v_tmp = {}
    #         for key, val in row.items():
    #             v_tmp.update({key.upper(): val})
    #         rows.append(v_tmp)
    #     # result['rows'] = rows
    #     result['data'] = sorted(rows, key=lambda x: x['FCREATE_TIME'], reverse=True)
    # else:
    #     result['data'] = sorted(result['rows'], key=lambda x: x[5], reverse=True)

    return flask.jsonify( result )


@authority.route("/rebut/apply/", methods=['POST', 'GET'])
@auth.gpv_required2
def authority_set_rebut_apply():
    """ 审批驳回
    """

    args = public_func.get_all_args(request.args, request.form)
    infoslist  = args.get('infoslist','')
    frebuts   = args.get('frebuts', '')
    infoslist = infoslist.split(",")

    applylist  = []

    for index,info in enumerate(infoslist):
        current_app.logger.warn(info)
        applylist.append([ int(data) for data in info.split('|') ][2])


    # if fdeal_uid != int(g.user_uid):
    #     return flask.jsonify( {'error_code':1001,'error_message':'你不是权限审批人，无权通过权限审批！'} )

    if not len(infoslist):
        return flask.jsonify( {'error_code':1002,'error_message':'error: 空应用信息！'} )

    result = authority_control.rebut_applys( frebuts, infoslist )

    if applylist:
        mail_messages = '你申请的游戏应用被驳回, 详情. <a href="http://data.oa.com/dc_new/#/authority/applylist?page=3"> http://data.oa.com/dc_new/#/authority/applylist?page=3 </a>'
        sendEmailExt(getNameList(applylist), mail_messages)

    if not result:
        return flask.jsonify( {'error_code':0,'error_message':'操作成功!'} )
    else:
        return flask.jsonify( {'error_code':result,'error_message':'操作有误，请联系管理员'})


@authority.route("/pass/apply/", methods=['POST', 'GET'])
@auth.gpv_required2
def pass_apply():
    """ 审批通过
    """

    args = public_func.get_all_args(request.args, request.form)
    infoslist  = args.get('infoslist','')

    infoslist = infoslist.split(",")
    applylist  = []

    for index,info in enumerate(infoslist):
        current_app.logger.warn(info)
        applylist.append([ int(data) for data in info.split('|') ][2])

    if not len(infoslist):
        return flask.jsonify({'error_code': 1002, 'error_message': 'error: 空应用信息！'})

    result = authority_control.pass_applys( infoslist)

    # 通过申请, 邮件告诉申请人
    if applylist :
        mail_messages = '你有通过申请的游戏应用, 详情. <a href="http://data.oa.com/dc_new/#/authority/applylist"> http://data.oa.com/dc_new/#/authority/applylist</a>';
        sendEmailExt( getNameList( applylist ), mail_messages )
    if result:
        return flask.jsonify({'error_code': 0, 'error_message': '操作成功!'})
    else:
        return flask.jsonify({'error_code': result, 'error_message': '操作有误，请联系管理员'})


@authority.route('/dc/user/list/')
@auth.gpv_required2
def dc_user_list():
    """ D系统获取用户列表
    """
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["table_format"] = "dc_user"

    result = authority_control.dc_user_lists(args)
    # result['rows'] = public.paging_func(result['rows'], page_size = int(page_size), page_num= int(page_num))
    return flask.jsonify(result)


@authority.route('/dc/user/info/')
@auth.gpv_required2
def dc_user_info():
    """ D系统获取用户列表
    """
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["fuid"] = args.get("fuid",0)
    if not args["fuid"]:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR,u'参数错误！'))

    result = authority_control.dc_user_info(args)
    # result['rows'] = public.paging_func(result['rows'], page_size = int(page_size), page_num= int(page_num))
    return flask.jsonify(result)


@authority.route("/user/root/",methods=['GET', 'POST'])
@auth.gpv_required2
def page_user_root():
    """更改用户角色
    将这个uid的用户角色重设为roleid
    """
    args = public_func.get_all_args(request.args, request.form)
    args["fm_uid"] = session["fm_uid"]
    args["fuid"] = args.get("fuid",0)
    args["roleid"] = args.get("roleid",0)
    result = {'code':1000,'message':'分配失败！'}

    #如果想将这个uid设为管理员，只有李**，王**有权利

    rv = authority_control.change_superuser(args["fuid"], args["roleid"])
    if rv:
        result = {'code':0,'message':'分配成功！'}

    return flask.jsonify(result)


@authority.route('/user/gpv/del/all/',methods=['GET', 'POST'])
@auth.gpv_required2
def user_gpv_del_all():
    args = public_func.get_all_args(request.args, request.form)
    fuid = args.get("fuid",0)
    if not fuid:
        return flask.jsonify({'error_code':1,'error_message':'删除失败！'})

    """
    删除指定用户所有权限
    """
    sql = """ delete from  byl_account_gpv_maps where fuid = %s""" % fuid
    if g.db.execute_rowcount(sql):
        return flask.jsonify({'error_code': 0,'error_message': '删除成功！'})
    else:
        return flask.jsonify({'error_code':1,'error_message':'删除失败！'})


@authority.route('/user/gpv/del/',methods=['GET', 'POST'])
@auth.gpv_required2
def user_gpv_del():
    """
    删除用户指定权限
    """
    args = public_func.get_all_args(request.args, request.form)
    args["fid"] = args.get("fid",'')
    # fsk = fsk.split(",")

    if not args["fid"]:
        return flask.jsonify({'error_code':1,'error_message':'删除失败！'})

    # sql = """ delete from  byl_account_gpv_maps where fid in (%s)""" % fid
    if authority_control.delete_pers(args):
        return flask.jsonify({'error_code': 0,'error_message': '删除成功！'})
    else:
        return flask.jsonify({'error_code':1,'error_message':'删除失败！'})


@authority.route('/depart/list/')
@auth.gpv_required2
def depart_list():
    """
    获取所有部门
    """

    sql = """  SELECT FDEPTID id, FDEPTNAME "name"
                    FROM authority_department_lists ORDER BY FDEPTID """

    result = g.db.query(sql)
    if result:
        return flask.jsonify({'data':result})
    else:
        return flask.jsonify({'data':[]})


@authority.route('/depart/user/list/')
@auth.gpv_required2
def depart_user_list():
    """
    获取所有用户
    """

    sql = """ SELECT bqa.FUID id,
                    bqa.fdisplay_name"name"
                    FROM byl_query_account bqa
                    WHERE bqa.fdisplay_name!='0'
                    ORDER BY "name" DESC """

    result = g.db.query(sql)
    if result:
        return flask.jsonify({'data':result})
    else:
        return flask.jsonify({'data':[]})

@authority.route("/principal/list/")
@auth.gpv_required2
def principal_list():
    """ 获取游戏终端语言的审批人列表
    """
    args = public_func.get_all_args(request.args, request.form)
    args["table_format"] = "principal_list"
    result = authority_control.principal_lists(args)
    return flask.jsonify(result)


@authority.route("/principal/delete/",methods=['GET', 'POST'])
@auth.gpv_required2
def principal_delete():
    """ 获取游戏终端语言的审批人列表
    """
    args = public_func.get_all_args(request.args, request.form)
    fsk = args.get("fsk", 0)
    if not fsk:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'参数错误！'))

    sql = """ DELETE FROM dcnew.authority_manage_info WHERE fsk = %s """ % int(fsk)

    if g.db.execute_rowcount(sql):

        return flask.jsonify(get_handle_result_code(helper.ErrorCode.SUCCESS,u'删除成功！'))
    else:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR,u'删除失败！'))


@authority.route("/principal/update/", methods=['POST', 'GET'])
@auth.gpv_required2
def principal_update():
    """ 更新审批人信息
    """
    args = public_func.get_all_args(request.args, request.form)

    args['fsk']     = args.get('fsk',0)
    args['fdeptid']     = args.get('fdeptid',0)
    args['fuid']     = args.get('fuid',0)

    result = False

    if not args['fsk'] or not args['fdeptid'] or not args['fuid']:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'参数错误！'))

    result = authority_control.principal_update(args)

    if result:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.SUCCESS,u'更新成功！'))
    else:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR,u'更新失败！'))


@authority.route("/principal/add/", methods=['POST', 'GET'])
@auth.gpv_required2
def principal_add():
    """ 添加审批人信息
    """
    args = public_func.get_all_args(request.args, request.form)

    args['fgamefsk'] = args.get('fgamefsk', 0)
    args['fterminaltypefsk'] = args.get('fterminaltypefsk', 0)
    args['flangtypefsk'] = args.get('flangtypefsk', 0)
    args['fdeptid'] = args.get('fdeptid', 0)
    args['fuid'] = args.get('fuid', 0)

    result = False

    if not args['fgamefsk'] or not args['fdeptid'] or not args['fuid']:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'参数错误！'))

    result = authority_control.principal_add(args)

    if result:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.SUCCESS, u'添加成功！'))
    else:
        return flask.jsonify(get_handle_result_code(helper.ErrorCode.ERROR, u'添加失败！'))


def sendEmailExt(lists, msg):
    # 发邮件

    # 为用户名加上域
    to_list = [ i + str('@boyaa.com') for i in lists ]
    warning_way.send_email( to_list, u'数据中心信息提醒', msg, 'html' )


#
def getNameList( lists ):
    # 去重, 为用户名加上域
    return [ authority_control.user_info( int(i) )['fname']  for i in list( set( lists ) ) ]

# -*- coding: utf-8 -*-
#公共工具类
import os
import datetime
import random
import re
import flask
import requests
import json
from flask import g, current_app, session
from libs import helper
from dc_redis_frame import cache_base
import redis_tools
import time
import sys
import json
reload (sys)
sys.setdefaultencoding("utf8")

def get_user_id_for_gpv(is_su):
    #如果用户为管理员，则设置uid为0 ，因为在f_get_gpvinfo 存储过程里是这么定义的
    #管理员可以查看所有的版本
    is_su = is_su if is_su else g.user_info.get('fis_su')
    if is_su:
        return 0

    sql_dict = {"uid" : g.user_info.get('fuid')}
    sql = """select * from analysis.byl_account_gpv_maps at
            where  fver_id = 0
            and fplat_id = 0
            and fgame_id = 0 and fuid=%(uid)s""" % sql_dict

    if g.db.query(sql):  # 如果有所有游戏权限也可以查看所有版本
        return 0
    return g.user_info.get('fuid')

def gen_bpid(bdict):
    return '|'.join([str(bdict.get("fgame_id", 0)), str(bdict.get("fplat_id", 0)), str(bdict.get("fhall_id", 0)),str(bdict.get("fsubgame_id", 0)),str(bdict.get("fterminal_id", 0)),str(bdict.get("fver_id", 0)),str(bdict.get("fchannel_id", 0))])

def format_version_chosen_data(rows = None,filters = None,chartype = "game"):
    if not rows:
        others_tmp = gen_default_result(filters)
    else:
        others_tmp = [{
                   "id": str(i.get("id", 0)),
                   "name": i.get("name","") if i.get("name","") else get_name_form_row(i.get("id", 0),chartype),
                   } for i in rows]
    final = {'data': others_tmp, }
    return final

def get_name_form_row(id_value,key):
    default_key_name = {"game" : "所有游戏",
            "plat":"所有平台",
            "hall":"所有大厅",
            "subgame":"所有子游戏",
            "terminal":"所有终端",
            "ver":"所有应用包",
            "lang":"所有语言",
            "channel":"所有渠道"}
    if int(id_value) == 0 :
        return unicode(default_key_name[key])
    return unicode(redis_tools.get_name_by_id(key,id_value))


# @todo 这个位置实现有点混乱
def gen_version_chosen_where_condition(filters,length,is_union = False):
    """
    is_union 这个位置是根据传进来的filters，是否需要检查存在所有权限的情况
    """

    table_keyword = ["fgame_id","fplat_id","fhall_id","fsubgame_id"," fterminal_id","fver_id","fchannel_id","flang_id"]
    gpv = filters
    gpv = gpv[0:length]
    condition = ""
    if is_union:
        condition = " AND %(key)s = %(value)s " % {"key" : table_keyword[length],"value" : 0}
        return condition

    table_keyword = table_keyword[0:length]
    for key, value in zip(table_keyword,gpv):
        #0表示所有，不过滤查询，fsubgame是独立于其他的字段的，所以不需要组合查询
        if value == "0" :
            continue
        if key == 'fsubgame_id':
            continue
        condition += "AND %(key)s = %(value)s " % {"key" : key,"value" : value}

    return condition

def gen_default_result(filters):
    return [{   "id" : "0",
                "name": "没有查询到数据",
                   }
           ]

def get_final_result(filters,sql,is_su,chartype):
    #根据用户的id，查询结果
    sql = sql % {"fuid" : get_user_id_for_gpv(is_su)}
    current_app.logger.warn(sql)
    datas = g.db.query(sql)
    return format_version_chosen_data(datas,filters,chartype)


def gen_version_query_sql(filters,table_name,cloumsdict,uninclude_char="",is_union = False):

    if is_union:
        return """select 0 as id,'%(name)s' as name,23333 as priority""" % {'name':get_name_form_row(0,(uninclude_char.split('_')[0])[1:])}

    filters = filters if filters else '0|0|0|0|0|0|0'
    filters = filters.split("|")
    table_keyword = ["fgame_id","fplat_id","fhall_id","fsubgame_id","fterminal_id","fver_id","fchannel_id","flang_id"]
    sql_dict = dict(zip(table_keyword,filters))
    if uninclude_char in table_keyword:
        try:
            del sql_dict[uninclude_char]
        except:
            pass

    sql = """select distinct """
    sql +=  ",".join(cloumsdict)
    sql +=  " from %(table_name)s where 2 > 1 %(condition)s"

    sql_dict["table_name"] = table_name
    current_app.logger.warn(filters)
    current_app.logger.warn(table_keyword.index(uninclude_char))
    current_app.logger.warn(is_union)
    current_app.logger.warn(sql_dict)
    current_app.logger.warn(sql)
    sql_dict["condition"] = gen_version_chosen_where_condition(filters,table_keyword.index(uninclude_char),is_union)
    sql = sql % sql_dict
    return sql

def get_user_gpvlist_permission(filters, is_su,chartype):
    """
    获取用户分配gpv列表
    满足用户选择单个gpv过滤
    选择用union是为了能够查询出有权限的所有的维度
    """
    if filters is None or len(filters.split("|")) != 7:
        return {"error":helper.ErrorCode.ARGS_ERROR}

    gpv_relation_dict = {
        "game" : """gen_version_query_sql(filters,"dcnew.f_get_gpvinfo(%%(fuid)s)",["fgame_id as id","fgame_name as name","priority as priority"],"fgame_id",%(is_union)s)""",
        "plat" : """gen_version_query_sql(filters,"dcnew.f_get_gpvinfo(%%(fuid)s)",["fplat_id as id","fplat_name as name","priority as priority"],"fplat_id",%(is_union)s)""",
        "hall" : """gen_version_query_sql(filters,"dcnew.f_get_gpvinfo(%%(fuid)s)",["fhall_id as id","fhall_name as name","priority as priority"],"fhall_id",%(is_union)s)""",
        "subgame" : """gen_version_query_sql(filters,"dcnew.subgame_map_fif",["fsubgame_id as id", "fsubgamename as name", "priority as priority"],"fsubgame_id",%(is_union)s)""",
        "terminal" : """gen_version_query_sql(filters,"dcnew.f_get_gpvinfo(%%(fuid)s)",["fterminal_id as id","fterminal_name as name","priority as priority"],"fterminal_id",%(is_union)s)""",
        "ver" :"""gen_version_query_sql(filters,"dcnew.f_get_gpvinfo(%%(fuid)s)",["fver_id as id","fver_name as name","priority as priority"],"fver_id",%(is_union)s)""",
        "channel" :""" gen_version_query_sql(filters,"dcnew.channel_map",["fchannel_id as id","fchannel_name as name","0 as priority"],"fchannel_id",%(is_union)s)""",
        "lang" : """gen_version_query_sql(filters,"dcnew.f_get_gpvinfo_status(%%(fuid)s,1)",["flang_id as id","flang_name as name","priority as priority"],"flang_id",%(is_union)s)""",
    }

    if chartype not in gpv_relation_dict.keys():
        return {"error":helper.ErrorCode.ARGS_ERROR}

    tmp_sql = gpv_relation_dict.get(chartype,"")
    #union查询如果有全部权限的时候
    if get_user_id_for_gpv(False) != 0 and (chartype not in ('channel','subgame')):
        sql = eval(tmp_sql % {"is_union" : False})
    else:
        sql = eval(tmp_sql % {"is_union" : False}) + " union "  +  eval(tmp_sql % {"is_union" : True})
    # 去重，排序
    sql = "select distinct a.id,a.name,sum(priority) pri from (%(sql)s) a  group by a.id,a.name HAVING id IS NOT NULL ORDER BY pri DESC" % {"sql" : sql}
    current_app.logger.info(sql)
    return get_final_result(filters, sql, is_su,chartype)


# 一旦用户选择之后gpv之后就记录，下次登录默认按这种gpv展示数据
def set_user_chosen_gpv_to_history(fuid,gpv,gpvname):

    insert_user_chosen_gpv_to_history(fuid, gpv, gpvname)
    return  helper.get_handle_result_code(helper.ErrorCode.SUCCESS)

def get_user_history_gpv(fuid):
    sql = "select distinct fgpvname,fgpvid,hisFocus from (select hid,fgpvid,fgpvname,coalesce(dui.id,0) as hisFocus from dcnew.user_chosen_gpv_history  cgh left JOIN dcnew.user_interest dui on cgh.fgpvid = dui.gpv and  cgh.fuid = dui.fuid where cgh.fuid = %(fuid)s order by hid desc limit 50) as tmp"
    sql_dict = {
        "fuid" : fuid,
    }
    datas = g.db.query(sql % sql_dict)
    result = []
    for data in datas:
        if '-' in data['fgpvid']:
            continue
        result.append(data)

    return {'data' : result}


def update_user_chosen_gpv_to_history(fuid,gpv,gpvname):

    sql = "update dcnew.user_chosen_gpv_history set fgpvname = '%(fgpvname)s',fgpvid = '%(fgpvid)s' where fuid = %(fuid)s"
    sql_dict = {
        "fuid" : fuid,
        "fgpvname":gpvname,
        "fgpvid" :gpv,
    }
    sql = sql % sql_dict
    g.db.execute(sql)
    return True

def insert_user_chosen_gpv_to_history(fuid,gpv,gpvname):

    today = datetime.date.fromtimestamp(time.time())
    sql = "insert into dcnew.user_chosen_gpv_history(fuid,fm_uid,fgpvname,fgpvid,fcreate_date) values(%(fuid)s, %(fm_uid)s,'%(fgpvname)s','%(fgpvid)s','%(fcreate_date)s')"
    sql_dict = {
        "fuid" : fuid,
        "fgpvname":gpvname,
        "fgpvid" :gpv,
        "fcreate_date" : today,
        "fm_uid" : g.user_info.get("fm_uid")
    }
    sql = sql % sql_dict
    g.db.execute(sql)
    return True

def update_user_interest_gpv_to_db(args_dict,table_name):

    interest_list = args_dict.get('datas',[])

    if type(interest_list) in (str,unicode):
        interest_list = json.loads(interest_list)
    interest_list = interest_list[0].get('items',[])
    sql_dict = [{"id":value.get('id',0),"priority":index} for index,value in enumerate(interest_list)]

    sql = "update dcnew.%(table_name)s set priority = %%(priority)s where id = %%(id)s" %{"table_name":table_name}
    g.db.executemany(sql,sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'更新关注成功')

def delete_user_gpv_group(id):
    fuid = g.user_info.get("fuid")
    sql_dict = {
        "fuid" : fuid,
        "id" : id,
    }
    sql = "delete from dcnew.user_gpv_groups where fuid = %(fuid)s and id = %(id)s"
    g.db.execute(sql % sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'删除汇总数据成功')


def get_user_gpv_group(ali_name = ''):
    result = []

    fuid = g.user_info.get("fuid")
    if len(ali_name):
        condition  = " and alian_name = '%(ali_name)s'" % {'ali_name' :ali_name}
    else:
        condition = ''
    sql_dict = {
     "fuid" : fuid,
     'condition' : condition
    }
    sql = """select alian_name,gpv_ids, gpv_names,id,priority from dcnew.user_gpv_groups where fuid = %(fuid)s %(condition)s order by priority""" % sql_dict
    datas = g.db.query(sql)
    for data in datas:
        final = {}
        temp = final.get(data['alian_name'], [])
        for gpv,gpv_name in zip(data['gpv_ids'].split('-'), data['gpv_names'].split('-')):
            temp.append({ 'gpv':gpv, 'gpv_name':gpv_name })
        final['data'] = temp
        final["gpv_name"] = data['alian_name']
        final['id']  = data['id']
        result.append(final)
    return {"data":result}


def update_user_gpv_group(alian_name,new_alian_name):
    fuid = g.user_info.get("fuid")
    sql_dict = {
        "fuid" : fuid,
        "alian_name" : alian_name,
        "new_alian_name" : new_alian_name,
    }

    sql = """
          select alian_name from dcnew.user_gpv_groups where fuid = %(fuid)s and alian_name = '%(new_alian_name)s'
          """
    datas = g.db.query(sql % sql_dict)

    if datas:
        return helper.get_handle_result_code(helper.ErrorCode.ERROR,u'该名称已经存在，请重新输入')
    sql = """update dcnew.user_gpv_groups set alian_name = '%(new_alian_name)s' where fuid = %(fuid)s and alian_name = '%(alian_name)s'"""
    g.db.execute(sql % sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'更新汇总数据成功')


def set_user_gpv_group(fuid,alian_name,gpv,gpv_name):
    fuid = g.user_info.get("fuid")
    sql_dict = {
        "fuid" : fuid,
        "alian_name" : alian_name,
        "gpv_name" : gpv_name,
        "gpv"  : gpv
    }
    sql = """
          select alian_name from dcnew.user_gpv_groups where fuid = %(fuid)s and alian_name = '%(alian_name)s'
          """
    datas = g.db.query(sql % sql_dict)
    if not datas:
        sql = """insert into dcnew.user_gpv_groups(fuid, alian_name, gpv_ids, gpv_names) values (%(fuid)s,'%(alian_name)s','%(gpv)s','%(gpv_name)s')"""

    else :
        return helper.get_handle_result_code(helper.ErrorCode.ERROR,u'该汇总名已经存在，请重新输入名字')
    g.db.execute(sql % sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'添加汇总数据成功')


def set_user_gpv_group_tmp(fuid,alian_name,gpv,gpv_name):
    fuid = g.user_info.get("fuid")
    sql_dict = {
        "fuid" : fuid,
        "alian_name" : alian_name,
        "gpv_name" : gpv_name,
        "gpv"  : gpv
    }

    sql = """insert into dcnew.user_gpv_tmp_group(fuid, alian_name, gpv_ids, gpv_names) values (%(fuid)s,'%(alian_name)s','%(gpv)s','%(gpv_name)s')"""

    g.db.execute(sql % sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'success')

def get_user_gpv_group_tmp():
    result = []

    fuid = g.user_info.get("fuid")
    sql_dict = {
     "fuid" : fuid
    }
    sql = """select alian_name,gpv_ids as gpv, gpv_names as gpv_name,id from dcnew.user_gpv_tmp_group where fuid = %(fuid)s order by id desc limit 1""" % sql_dict
    datas = g.db.query(sql)
    for data in datas:
        final = {}
        temp = final.get(data['alian_name'], [])
        for gpv,gpv_name in zip(data['gpv'].split('-'), data['gpv_name'].split('-')):
            temp.append({ 'gpv':gpv, 'gpv_name':gpv_name })
        final['data'] = temp
        final["gpv_name"] = data['alian_name']
        final['id']  = data['id']
        result.append(final)
    return {"data":result}


def set_user_interest_gpv_to_db(gpv,gpv_name):
    fuid = g.user_info.get("fuid")
    sql_dict = {
        "fuid" : fuid,
        "gpv_name" : gpv_name,
        "gpv"  : gpv
    }
    sql = """
          select gpv,gpvname from dcnew.user_interest where fuid = %(fuid)s and gpv = '%(gpv)s' and gpvname = '%(gpv_name)s'
          """
    datas = g.db.query(sql % sql_dict)
    if not datas:
        sql = """insert into dcnew.user_interest(fuid,gpv,gpvname) values (%(fuid)s,'%(gpv)s','%(gpv_name)s')"""
        g.db.execute(sql % sql_dict)
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'添加关注成功')

def get_user_interst_pgv_by_fuid():
    fuid = g.user_info.get("fuid")
    sql = "select id,gpv,gpvname as gpv_name,priority from dcnew.user_interest where fuid = %(fuid)s order by priority" % {"fuid" : fuid}

    datas = g.db.query(sql)
    return {"data" : datas,}

def delete_user_interst_pgv_by_id(id):
    sql = "delete from dcnew.user_interest where id = %(id)s" % {"id": id}
    #删除数据，没有删除一条也算成功
    try:
        datas = g.db.execute(sql)
    except:
        pass
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS,u'删除成功')

def gen_final_gpv_sql(fm_uid,condition):
    table_keyword = ["fgame_id","fplat_id","fhall_id","fterminal_id","fver_id","priority"]
    sql = "select "  + ",".join(table_keyword) + " from dcnew.f_get_gpvinfo(%(fm_uid)s) where 2 >1 %(condition)s order by priority desc limit 1"
    sql_dict = {"fm_uid" : fm_uid, "condition" : condition}
    sql = sql % sql_dict

    current_app.logger.info(sql)
    datas = g.db.query(sql)
    return datas

#@todo
def has_user_gpv_permission(input_pgv,gpv_name,is_save = True):
    """
    用户有可能在版本选择器里面直接选了其中某一个版本就直接提交了，
    这样前台传过来的数据里，未选择的默认为0，然而这B可能并没所有的权限
    此时直接报错
    """
    if not input_pgv:
        return False
    names = input_pgv.split("|")
    fuid = get_user_id_for_gpv(False)
    fm_uid = g.user_info.get("fm_uid")

    condition = " AND (fgame_id=%(fgame_id)s or fgame_id = 0 ) AND (fplat_id=%(fplat_id)s or fplat_id = 0) AND (fver_id=%(fver_id)s or fver_id = 0)" %{ "fgame_id" :names[0], "fplat_id":names[1], "fver_id": names[5]}
    result = gen_final_gpv_sql(fuid, condition)

    if not result:
        sql = "select fplat_id,fver_id,fhall_id,fterminal_id from dcnew.f_get_gpvinfo(%(fm_uid)s) where fgame_id=%(fgame_id)s or fgame_id = 0" % {"fgame_id" :names[0],'fm_uid':fuid}
        datas = g.db.simple_query(sql)
        current_app.logger.info(datas)
        fplat_ids = [x[0] for x in datas]
        fver_ids = [x[1] for x in datas]
        fhall_ids = [x[2] for x in datas]
        fterminal_ids = [x[3] for x in datas]
        if long(names[1]) not in fplat_ids:
            return False,u"没有所有平台权限，请选择一个平台.",u'平台'
        if long(names[2]) not in fhall_ids:
            return False,u"没有所有大厅权限，请选择一个大厅.",u'大厅'
        if long(names[4]) not in fterminal_ids:
            return False,u"没有所有终端权限，请选择一个终端.",u'终端'
        if long(names[5]) not in fver_ids:
            return False,u"没有所有应用包权限，请选择一个应用包.",u'应用包'

    fuid = g.user_info.get("fuid")
    if is_save:
        set_user_chosen_gpv_to_history(fuid, input_pgv, gpv_name)

    return True,'',''

#本函数是为了实现当用户没有权限的时候默认给用户一个权限，默认获取第一个
#但是现在经过多方讨论，决定当用户选择的组合没有权限的时候，直接报错就行了
def gen_user_gpv_within_promission_old_not_use(input_pgv,gpv_name,is_save= True):
    """
    用户有可能在版本选择器里面直接选了其中某一个版本就直接提交了，
    这样前台传过来的数据里，未选择的默认为0，然而这B可能并没所有的权限
    此时生成默认的用户有权限的
    此函数暂时没有使用
    """
    gpv = input_pgv if input_pgv else "0|0|0|0|0|0|0"
    names = gpv.split("|")
    fuid = get_user_id_for_gpv(False)
    fm_uid = g.user_info.get("fm_uid")

    if ('0' in [names[0],names[1],names[5]]) and  fuid != 0:

        condition = gen_version_chosen_where_condition(names, 6, is_union=False)
        result = gen_final_gpv_sql(fuid, condition)

        if not result:
            return "",""
        result = result[0]
        gpv_id = [result["fgame_id"],result["fplat_id"],result["fhall_id"],int(names[3]),result["fterminal_id"],result["fver_id"],int(names[-1])]
        keys  = ["game" ,"plat", "hall","subgame","terminal","ver","channel"]
        gpv_name = "|".join([get_name_form_row(id,key) for key,id in zip(keys,gpv_id)])
        gpv = "|".join([str(x) for x in gpv_id])

    #获取用户的实际fuid
    fuid = g.user_info.get("fuid")
    if is_save:
        set_user_chosen_gpv_to_history(fuid, gpv, gpv_name)

    return gpv, gpv_name


def check_gpv_has_promission(args_gpv):
    has_permission,info,key = has_user_gpv_permission(args_gpv, '')
    if not has_permission:
        final = helper.get_handle_result_code(helper.ErrorCode.NO_GPV_PEMSSION, info)
        final.update({'key':key})
        current_app.logger.info(final)
        return final
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS, u'success')

def get_bpid_list(args_gpv):
    #首先检查权限
    # has_permission,info,key = has_user_gpv_permission(args_gpv, '')
    # # if not has_permission:
    # #     final = helper.get_handle_result_code(helper.ErrorCode.NO_GPV_PEMSSION, info)
    # #     final.update({'data':[]})
    # #     current_app.logger.info(final)
    # #     return final
    fuid = get_user_id_for_gpv(False)
    keywords = ['fgame_id','fplat_id','fhall_id','fterminal_id','fver_id']
    values = args_gpv.split('|')
    query = ''
    for key,value in zip(keywords,values):
        if value in [0,'0']:
            continue
        query += ' and %(key)s = %(value)s' % {'key':key,'value':value}
    sql = "select bpid from dcnew.f_get_gpvinfo_status_all_with_bpid(%(fuid)s,1) where 2 > 1 %(query)s" % {'fuid':fuid,'query':query}
    current_app.logger.info(sql)
    datas = g.db.query(sql)
    final = helper.get_handle_result_code(helper.ErrorCode.SUCCESS, u'success')
    final.update({'data':datas})
    return final

def set_select_gpv_to_redis(args_gpv, args_gpv_name, auth):
    """
    在设置的时候不校验用户是否有所设置gpv的权限，统一在取数据之前验证
    """
    has_permission,info,key = has_user_gpv_permission(args_gpv, args_gpv_name)
    if not has_permission:
        final = helper.get_handle_result_code(helper.ErrorCode.NO_GPV_PEMSSION, info)
        final.update({'key':key})
        current_app.logger.info(final)
        return final

    select_gpv = cache_base.UserSelectGPV( session.get('fm_uid') )

    # 将gpv设置到redis中
    select_gpv.set_gpv_list([args_gpv])
    g.gpv = [args_gpv]
    g.gpv_name = args_gpv_name

    select_gpv.set_gpv_name(args_gpv_name)

    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS, u'success')


def set_select_gpv_group_to_redis(post_data):
    """
    在设置的时候不校验用户是否有所设置gpv的权限，统一在取数据之前验证
    """
    current_app.logger.warning(post_data)
    gpv_list = post_data.get("gpv",'').split(',')
    current_app.logger.warning(gpv_list)
    gpv_names = post_data.get("gpv_name",'').split(',')
    alians_name = post_data.get("ali_name",'多版本-汇总数据')
    for gpv,gpv_name in zip(gpv_list, gpv_names):
        has_permission,info,key = has_user_gpv_permission(gpv, gpv_name,False)
        if not has_permission:
            return helper.get_handle_result_code(helper.ErrorCode.NO_GPV_PEMSSION, info)

    select_gpv = cache_base.UserSelectGPV( session.get('fm_uid') )

    # 将gpv设置到redis中
    select_gpv.set_gpv_list(gpv_list)
    g.gpv = gpv_list
    g.gpv_name = alians_name

    select_gpv.set_gpv_name(alians_name)
    fuid = g.user_info.get("fuid")
    set_user_chosen_gpv_to_history(fuid, '-'.join(gpv_list), alians_name)
    if  alians_name != '多版本-汇总数据':
        set_user_gpv_group(fuid,alians_name,'-'.join(gpv_list),'-'.join(gpv_names))
    else :
        set_user_gpv_group_tmp(fuid,alians_name,'-'.join(gpv_list),'-'.join(gpv_names))
    return helper.get_handle_result_code(helper.ErrorCode.SUCCESS, u'success')


if __name__ == "__main__":
    pass
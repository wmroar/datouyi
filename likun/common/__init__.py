
#encoding:utf-8
from project_common.pro_auth import ProjectAuth
from flask import current_app, session,g,request
from dc_redis_frame import cache_base
import re
import requests
import urllib
from urllib import urlencode
import json
import redis_tools
from libs import helper
import datetime
import time

class Auth(ProjectAuth):

    def get_admin_uid(self):
        """
        获取用户uid
        此函数为什么单独提出来是，为了多个项目分别利用不同的用户进行调试
        """
        #TODO 这里修改为了调试方便
        if current_app.config['DEBUG']:
            admin_uid = current_app.config['DEBUGER']
            session['fm_uid'] = admin_uid
            session['fm_cname'] = urllib.unquote(str("%E6%9F%B3%E5%8B%A4%E6%9E%97")).decode("utf-8")

        else:
            session_fm_uid = request.cookies.get("admin_uid",None)
            session_fm_cname = request.cookies.get("admin_cname",None)
            session["fm_cname"] = urllib.unquote(str(session_fm_cname)).decode("utf-8")
            admin_uid = int(session_fm_uid) if session_fm_uid else None
            if not session.get('fm_uid',None) :
                session["fm_uid"] = admin_uid


            # admin_uid = 797
            # session['fm_uid'] = 797
        current_app.logger.warn(session)
        return session["fm_uid"]

    # 这里是七维的，但是权限表里仍然是三维的，所以，我们这里只取其中三维进行验证
    # 这个位置比较别扭，应该可以将权限表进行改进
    def get_gpvs_by_user(self, fuid, input_gpv):
        """
        用户uid信息获取用户拥有权限的版本信息
        """
        g, p,h,s,t,v,c = tuple(input_gpv.split('|'))

        test_gpv = g + "|" + p + "|" + v

        select_gpv_list = [test_gpv, g + '|' + p + '|0', g + '|0|0', '0|0|0']

        for select_gpv in select_gpv_list:
            gpv = cache_base.UserGPVCacheEntity(
                fuid, select_gpv).get_cache_data()
            # 如果其中任何一个存在都表示当前版本合格
            if gpv:
                return input_gpv

        return True

    def get_gpv_user_default(self, fm_uid):
        """初始化用户gpv信息
        """
        assert(fm_uid != None)
        sql = """select fgpvid as gpv,fgpvname as gpvname from dcnew.user_chosen_gpv_history where fm_uid = %(fuid)s
                    order by hid desc limit 1""" % {"fuid" : fm_uid}
        u_gpv = g.db.get(sql)
        if not u_gpv:
            # 取不到就取用户权限列表里面最后一条
            sql = """select concat(fgame_id, '|', fplat_id, '|0|0|0|', fver_id,'|0') gpv,'' as gpvname
            from (select fgame_id, fplat_id, fver_id,
                    row_number() over(partition by fm_uid order by fid desc) rown
                    from analysis.byl_account_gpv_maps ss where fm_uid = '%s' and fstatus = 1
            ) as abc where rown = 1""" % fm_uid
            u_gpv = g.db.get(sql)

        if u_gpv:
            gpv = u_gpv.gpv.split('-')
            gpv_name = u_gpv.gpvname
        else:
            gpv = None
            gpv_name = ''
        return gpv,gpv_name

    def is_need_gpv_valid(self,gpv):
        if gpv is None:
            return False
        gpv = re.sub("%7C","|",gpv)
        if len(gpv.split("|")) != 7:
            return False
        return True

    def get_name_form_row(self,id_value,key):
        if int(id_value) == 0 :
            return ""
        return unicode(redis_tools.get_name_by_id(key,id_value))

    def get_gpv_name(self,gpv):
        final = []
        filters = gpv.split("|")
        keydict = ["game","plat" ,"hall","subgame","terminal","ver","channel"]
        for key ,value in zip(filters, keydict):
            final.append(self.get_name_form_row(key,value))

        if final:
             return "|".join(final)
        else:
            return "||||||"

    def get_user_info(self, admin_uid):
        """
        获取用户信息
        """
        user_info = cache_base.UserCacheEntity(admin_uid).get_cache_data()
        return user_info

    def _gpv_required_impl(self):

        fm_uid = self.get_admin_uid()
        # 表示用户第一次进入gpv为空, 设置用户之前的版本
        if not g.gpv:
            select_gpv = cache_base.UserSelectGPV(fm_uid)
            current_app.logger.info(self.get_gpv_user_default(fm_uid))
            g.gpv,g.gpv_name = self.get_gpv_user_default(fm_uid)
            # 用户没有权限
            if not g.gpv:
                if str(g.user_info['fis_su']) == '1':
                    g.gpv = ["1396895|58930167|0|0|0|0|0"]
                else :
                    return helper.get_handle_result_code(helper.ErrorCode.NO_GPV)
            if not g.gpv_name:
                current_app.logger.info(g.gpv)
                g.gpv_name = self.get_gpv_name(g.gpv[0])

            # 存入缓存
            select_gpv.set_gpv_list(g.gpv)
            select_gpv.set_gpv_name(g.gpv_name)

        # 表示用户之前设置过gpv，检验版本权限
        else:
            # 管理员不做认证
            if str(g.user_info['fis_su']) == '1':
                return None

            # 单版本选择
            if len(g.gpv) == 1:
                redis_gpv = self.get_gpvs_by_user(
                    g.user_info['fuid'], g.gpv[0])

                if not redis_gpv:
                    return helper.get_handle_result_code(helper.ErrorCode.NO_GPV)
            # 多版本校验, 校验头，中，尾。考虑到校验性能
            else:
                for gpv in [g.gpv[0], g.gpv[-1], g.gpv[len(g.gpv) / 2]]:

                    redis_gpv = self.get_gpvs_by_user(g.user_info['fuid'], gpv)
                    if not redis_gpv:
                        return helper.get_handle_result_code(helper.ErrorCode.NO_GPV)

        return None
    def save(self, uid, name, display_name, src = 1):

        account_id = 0
        try:
            account_id = g.db.get("select fuid from byl_query_account where fm_uid = '%s' and fm_src = %s" % (uid, src))
        except:
            pass
        else:
            if not account_id:
                g.db.execute_rowcount("""insert into byl_query_account ( fm_uid, fm_src, fname, fdisplay_name, fcreate_at )
                    values ( '%s', %s, '%s', '%s',to_date('%s','yyyy-mm-dd hh24:mi:ss') )
                    """ % (uid, src, name, display_name, datetime.datetime.fromtimestamp(int(time.time())))
                                      )
                # //user_uid
                a = g.db.get("select fuid from byl_query_account where fm_uid = '%s' and fm_src = %s" % (uid, src))
                if a:
                    g.user_uid = a.fuid
            try:
                _sql = """UPDATE byl_query_account
                                SET flogin_at = CURRENT_TIMESTAMP
                                WHERE fm_uid = '%s' """ % (uid,)
                g.db.execute_rowcount(_sql)
                g.user_uid = account_id.fuid
            except:
                pass

    def get_user_gpv(self):
        """获取gpv
        """
        gpv = None
        gpv_name = None
        current_app.logger.info('in get_user_gpv')
        fm_uid = session.get("fm_uid")
        if fm_uid :
            select_gpv = cache_base.UserSelectGPV(fm_uid)
            # 从缓存中取
            gpv = select_gpv.get_gpv_list()
            current_app.logger.warning(gpv)
            gpv_name = select_gpv.get_gpv_name()

            # 用户的gpv信息在redis还不存在
            if not gpv:
                gpv,gpv_name = self.get_gpv_user_default(fm_uid)
                current_app.logger.info(gpv)
                if gpv:
                    if not gpv_name:
                        gpv_name = self.get_gpv_name(gpv[0])
                    # 存入缓存
                    select_gpv.set_gpv_list(gpv)
                    select_gpv.set_gpv_name(gpv_name)
        return gpv, gpv_name

auth = Auth()
# -*- coding: utf-8 -*-
"""
维度命名约定:
分布维度 ：sp
新增：r
活跃：a
牌局：p
游戏币：g
付费：

"""
import datetime #导入日期时间模块
today = datetime.date.today()
yesterday =  datetime.datetime.strftime(today - datetime.timedelta(days=1),"%Y-%m-%d")
lastweekday = datetime.datetime.strftime(today - datetime.timedelta(days=7),"%Y-%m-%d")
today = datetime.datetime.strftime(today,"%Y-%m-%d")

dim_labels = {


'fis_disable'      : {'cn':u'日报是否对其可见',},
'fdate'            : {'cn':u'日期',},
'FPLATFORMFSK'     : {'cn':u'平台',},
'FGAMEFSK'         : {'cn':u'游戏',},
'FVERSIONFSK'      : {'cn':u'版本',},
'FTERMINALFSK'     : {'cn':u'终端',},
'FLANGTYPENAME'    : {'cn':u'语言'},
'FDISTRICTNAME'    : {'cn':u'区域'},
'users'            : {'cn':u'用户数'},


'gamename'        :{'cn':u'游戏'},
'platformname'    :{'cn':u'平台'},
'hallname'        :{'cn':u'大厅'},
'versionname'     :{'cn':u'版本'},
'terminaltypename':{'cn':u'终端'},
'packagename'     :{'cn':u'应用包'},
'langtypename'    :{'cn':u'语言'},
'lianyun'         :{'cn':u'是否联运'},
'bpid'            :{'cn':u'BPID'},
'bpid_key'        :{'cn':u'BPID_KEY'},
'apply_date'      :{'cn':u'申请日期'},
'fremark'         :{'cn':u'备注'},
'dealer'          :{'cn':u'当前处理人'},
'applyer'         :{'cn':u'申请人'},
'app_kind'         :{'cn':u'应用类型'},
'app_name'         :{'cn':u'应用名称'},


'gamename'         :{'cn':u'游戏',},
'platname'         :{'cn':u'平台',},
'defname'          :{'cn':u'自定义分类名称',},
'fcreater'         :{'cn':u"创建人"},
'fmodifier'        :{'cn':u"最后修改人"},
'fchangetime'      :{'cn':u"最后修改时间"},



#用户付费
'darpu'            :{'cn':u'日ARPPU','sf':'not_use'},
'dip'              :{'cn':u'付费总额','sf':'not_use'},
'dpu'              :{'cn':u'付费用户数','sf':'not_use'},
'dspu'             :{'cn':u'首付用户数','sf':'not_use'},
'pur'              :{'cn':u'付费渗透率','sf':'not_use'},
'dpcnt'            :{'cn':u'付费次数','sf':'not_use'},
'dau'              :{'cn':u'日活跃用户','sf':'not_use'},
'dslip'            :{'cn':u'首付总额','sf':'not_use'},
'7darpu'           :{'cn':u'周ARPPU','sf':'not_use'},
'7dip'             :{'cn':u'7日充值总额','sf':'not_use'},
'7dpu'             :{'cn':u'7日付费用户数','sf':'not_use'},
'7dspu'            :{'cn':u'7日首付用户数','sf':'not_use'},
'7dpur'            :{'cn':u'7日付费渗透率','sf':'not_use'},
'7dpcnt'           :{'cn':u'7日付费次数','sf':'not_use'},
'7dau'             :{'cn':u'周活跃用户','sf':'not_use'},
'7dslip'           :{'cn':u'7日首付总额','sf':'not_use'},
'30darpu'          :{'cn':u'月ARPPU','sf':'not_use'},
'30dip'            :{'cn':u'30日充值总额','sf':'not_use'},
'30dpu'            :{'cn':u'30日付费用户数','sf':'not_use'},
'30dspu'           :{'cn':u'30日首付用户数','sf':'not_use'},
'30dpur'           :{'cn':u'30日付费渗透率','sf':'not_use'},
'30dpcnt'          :{'cn':u'30日付费次数','sf':'not_use'},
'30dau'            :{'cn':u'月活跃用户数','sf':'not_use'},
'30dslip'          :{'cn':u'30日首付总额','sf':'not_use'},





'pay_def'          :{'cn':u"收入自定义",'sf':'pay_def'},
'fdefname'         :{'cn':u"收入自定义名称"},
'uidtag'           :{'cn':u"用户ID(标签)"},


'sp_assets'        :{'cn':u'用户资产分布', 'sf':'sp_assets'} ,
'sp_paynum'        :{'cn':u'付费额度分布', 'sf':'sp_paynum'} ,
'sp_paycnt'        :{'cn':u'付费次数分布', 'sf':'sp_paycnt'} ,
'sp_bankrupt'      :{'cn':u'破产次数分布', 'sf':'sp_bankrupt'} ,
'sp_party'         :{'cn':u'玩牌局数分布', 'sf':'sp_party'} ,
'sp_party_reg'         :{'cn':u'玩牌局数分布', 'sf':'sp_party_reg'} ,
'sp_party_active'         :{'cn':u'玩牌局数分布', 'sf':'sp_party_active'} ,
'sp_hourr'         :{'cn':u'时段新增', 'sf':'sp_hourr'} ,
'spu_hourr'        :{'cn':u'时段-登陆人数', 'sf':'sp_hourr'} ,
'spn_hourr'        :{'cn':u'时段-登陆次数', 'sf':'sp_hourr'} ,
'spp_hourr'        :{'cn':u'时段-玩牌人数', 'sf':'sp_hourr'} ,

'sp_ver_num'       :{'cn':u'版本分布', 'sf':'sp_ver'},
'sp_ver_dnum'      :{'cn':u'版本分布(设备数)', 'sf':'sp_ver'},

'spr_source'       :{'cn':u'新增用户来源分布', 'sf':'spr_source'},
'spa_source'       :{'cn':u'活跃用户来源分布', 'sf':'spa_source'},
'spr_spath'        :{'cn':u'新增用户来源路径分布', 'sf':'sp_spath'},
'spa_spath'        :{'cn':u'活跃用户来源路径分布', 'sf':'sp_spath'},

'spr_gender'       :{'cn':u'新增用户性别分布', 'sf':'spr_gender'},
'spa_gender'       :{'cn':u'活跃用户性别分布', 'sf':'spa_gender'},


"spr_entrance_num" :{'cn':u'账号类型分布', 'sf':'sp_entrance'},
"spr_entrance_dnum":{'cn':u'账号类型分布(设备数)', 'sf':'sp_entrance'},
"spa_entrance_num" :{'cn':u'账号类型分布', 'sf':'sp_entrance'},
"spa_entrance_dnum":{'cn':u'账号类型分布(设备数)', 'sf':'sp_entrance'},

"spr_chan"         :{'cn':u'(新增)渠道分布', 'sf':'sp_chan'},
"spa_chan"         :{'cn':u'(活跃)渠道分布', 'sf':'sp_chan'},


"spr_ad"           :{'cn':u'(新增)广告分布', 'sf':'sp_ad'},
"spa_ad"           :{'cn':u'(新增)广告分布', 'sf':'sp_ad'},
"sp_age"           :{'cn':u'用户年龄分布', 'sf':'sp_age'},
"sp_level"         :{'cn':u'用户等级分布', 'sf':'sp_level'},
"sp_hispay"        :{'cn':u'历史付费活跃', 'sf':'sp_hispay'},
"sp_lang"          :{'cn':u'用户语言分布', 'sf':'sp_lang'},
"spa_interval"     :{'cn':u'活跃间隔', 'sf':'spa_interval'},

#赛事分析
'fbs_payusernum'   :{'cn':u'付费人数', 'sf':'bs_pay'} ,
'fbs_paycnt'       :{'cn':u'付费次数', 'sf':'bs_pay'} ,
'fbs_paycnt_per'   :{'cn':u'人均付费次数', 'sf':'bs_pay'} ,
'fbs_income'       :{'cn':u'付费金额', 'sf':'bs_pay'} ,
'fbs_income_per'   :{'cn':u'人均付费金额', 'sf':'bs_pay'} ,
'fbs_umaxpcnt'     :{'cn':u'单用户最多付费次数', 'sf':'bs_pay'} ,
'fbs_umaxincome'   :{'cn':u'用户单次最高付费金额', 'sf':'bs_pay'} ,

'fpapplyucnt'      :{'cn':u'新增报名人数','sf':'bs_newadd'},
'fnapplyucnt'      :{'cn':u'新增报名人数','sf':'bs_newadd'},
'fsapplyucnt'      :{'cn':u'新增报名人数','sf':'bs_newadd'},
'fgapplyucnt'      :{'cn':u'新增报名人数','sf':'bs_newadd'},

'fppartyucnt'      :{'cn':u'新增参赛人数','sf':'bs_newadd'},
'fnpartyucnt'      :{'cn':u'新增参赛人数','sf':'bs_newadd'},
'fspartyucnt'      :{'cn':u'新增参赛人数','sf':'bs_newadd'},
'fgpartyucnt'      :{'cn':u'新增参赛人数','sf':'bs_newadd'},

'fpregappucnt'     :{'cn':u'新增注册报名人数','sf':'bs_newadd'},
'fnregappucnt'     :{'cn':u'新增注册报名人数','sf':'bs_newadd'},
'fsregappucnt'     :{'cn':u'新增注册报名人数','sf':'bs_newadd'},
'fgregappucnt'     :{'cn':u'新增注册报名人数','sf':'bs_newadd'},

'fpregpartyucnt'   :{'cn':u'新增注册参赛人数','sf':'bs_newadd'},
'fnregpartyucnt'   :{'cn':u'新增注册参赛人数','sf':'bs_newadd'},
'fsregpartyucnt'   :{'cn':u'新增注册参赛人数','sf':'bs_newadd'},
'fgregpartyucnt'   :{'cn':u'新增注册参赛人数','sf':'bs_newadd'},

'fppartyucnt_hb'   :{'cn':u'新增参赛人数环比(%)','sf':'bs_newadd'},
'fnpartyucnt_hb'   :{'cn':u'新增参赛人数环比(%)','sf':'bs_newadd'},
'fspartyucnt_hb'   :{'cn':u'新增参赛人数环比(%)','sf':'bs_newadd'},
'fgpartyucnt_hb'   :{'cn':u'新增参赛人数环比(%)','sf':'bs_newadd'},

'fpregappucnt_hb'  :{'cn':u'新增注册报名人数环比(%)','sf':'bs_newadd'},
'fnregappucnt_hb'  :{'cn':u'新增注册报名人数环比(%)','sf':'bs_newadd'},
'fsregappucnt_hb'  :{'cn':u'新增注册报名人数环比(%)','sf':'bs_newadd'},
'fgregappucnt_hb'  :{'cn':u'新增注册报名人数环比(%)','sf':'bs_newadd'},

#前端传过来的dims
'fapplyucnt_n'     :{'cn': '新增报名人数','sf':'bs_newadd'},
'fpartyucnt_n'     :{'cn': '新增参赛人数','sf':'bs_newadd'},
'fpartyucnt_hb_n'  :{'cn': '新增参赛人数环比(%)','sf':'bs_newadd'},
'fregappucnt_n'    :{'cn': '新增注册报名人数','sf':'bs_newadd'},
'fregappucnt_hb_n' :{'cn': '新增注册报名人数环比(%)','sf':'bs_newadd'},
'fregpartyucnt_n'  :{'cn': '新增注册参赛人数','sf':'bs_newadd'},


'spr_bs_pltime'    :{'cn':u'用户参赛时长分布','sf':'spr_bs_pltime'},


'fapplyucnt'       :{'cn':u'报名人数', 'sf':'bs_outline'},
'fapplyucnt_hb'    :{'cn':u'报名人数环比(%)','sf':'bs_outline'},
'fapplycnt'        :{'cn':u'报名人次', 'sf':'bs_outline'},
'fpartyucnt'       :{'cn':u'参赛人数', 'sf':'bs_outline'},
'fpartyucnt_hb'    :{'cn':u'参赛人数环比(%)','sf':'bs_outline'},
'fpartycnt'        :{'cn':u'参赛人次', 'sf':'bs_outline'},
'fpc_ac_cr'        :{'cn':u'报名参赛转化率', 'sf':'bs_outline'},
'fwinusernum'      :{'cn':u'获奖人数', 'sf':'bs_outline'},
'fwu_pu_cr'        :{'cn':u'参赛获奖率', 'sf':'bs_outline'},
'fautoquitnum'     :{'cn':u'自动退赛人数', 'sf':'bs_outline'},
'fsysquitnum'      :{'cn':u'系统退赛人数', 'sf':'bs_outline'},
'fmatchnum'        :{'cn':u'开赛次数', 'sf':'bs_outline'},

'dsu'              :{'cn':u'新增用户数','sf':'not_use'},
'dau'              :{'cn':u'活跃用户数','sf':'not_use'},
'7dau'             :{'cn':u'周活跃用户数','sf':'not_use'},
'30dau'            :{'cn':u'月活跃用户数','sf':'not_use'},
'rdau'             :{'cn':u'日活跃/月活跃','sf':'not_use'},
'logincnt'         :{'cn':u'登录次数','sf':'not_use'},
'pun'              :{'cn':u'玩牌用户数','sf':'not_use'},
'dip'              :{'cn':u'付费金额','sf':'not_use'},
'dlogun'           :{'cn':u'登陆用户数','sf':'not_use'},
'dubrc'            :{'cn':u'破产用户数','sf':'not_use'},
'dgsun'            :{'cn':u'金流用户数','sf':'not_use'},
'dpur'             :{'cn':u'付费渗透率%','sf':'not_use'},
'1dsur'            :{'cn':u'新增1日留存率','sf':'not_use'},
'7dsur'            :{'cn':u'新增7日留存率','sf':'not_use'},
'14dsur'           :{'cn':u'新增14日留存率','sf':'not_use'},
'30dsur'           :{'cn':u'新增30日留存率','sf':'not_use'},
'60dsur'           :{'cn':u'新增60日留存率','sf':'not_use'},
'90dsur'           :{'cn':u'新增90日留存率','sf':'not_use'},
'dhpu'             :{'cn':u'新增付费转化率','sf':'not_use'},
'dsupun'           :{'cn':u'新增玩牌转化率','sf':'not_use'},
'dsu_rupt'         :{'cn':u'新增用户破产率','sf':'not_use'},
'dsupaycnt'        :{'cn':u'用户新增-付费次数','sf':'not_use'},
'dpucnt'           :{'cn':u'当日付费用户','sf':'not_use'},
'dsuip'            :{'cn':u'付费额度','sf':'not_use'},
'spun'             :{'cn':u'注册玩牌人数','sf':'not_use'},
'dsupuncnt'        :{'cn':u'玩牌次数','sf':'not_use'},
'dsulogcnt'        :{'cn':u'登陆次数','sf':'not_use'},
'tsu'              :{'cn':u'累增用户数','sf':'not_use'},
'bur'              :{'cn':u'破产率','sf':'not_use'},
'lcpunp'           :{'cn':u'活跃玩牌率','sf':'not_use'},
'lcregpunp'        :{'cn':u'注册玩牌率','sf':'not_use'},
'lcretpunp'        :{'cn':u'回流用户玩牌率','sf':'not_use'},
'darpu'            :{'cn':u'日ARPU','sf':'not_use'},
'charge'           :{'cn':u'台费消耗','sf':'not_use'},
'pucnt'            :{'cn':u'玩牌人次','sf':'not_use'},
'partyn'           :{'cn':u'牌局数','sf':'not_use'},
'partytime'        :{'cn':u'牌局时长（小时）','sf':'not_use'},
'apartytime'       :{'cn':u'单局平均时间（秒）','sf':'not_use'},
'alltime'          :{'cn':u'玩牌时长(小时)','sf':'not_use'},
'aplayusertime'    :{'cn':u'人均玩牌时长(分)','sf':'not_use'},
'paypartynum'      :{'cn':u'付费用户牌局数','sf':'not_use'},
'payusernum'       :{'cn':u'付费玩牌用户数','sf':'not_use'},
'partyn_avg'       :{'cn':u'人均玩牌次数','sf':'not_use'},

#在线在玩
'ou'           :{'cn':u'在线实时','sf':'real_time'},
'opu'          :{'cn':u'在玩实时','sf':'real_time'},
'fparty_type'  :{'cn':u'场次类型'},

#牌局概览
'spun'         :{'cn':u'注册玩牌人数','sf':'sp_spun'},
'sp_1drpun'    :{'cn':u'昨注玩牌人数','sf':'sp_1drpun'},
'sp_pn'        :{'cn':u'牌局数','sf':'sp_pn'},
'sp_actpn'     :{'cn':u'活跃牌局','sf':'sp_actpn'},
'sp_ybackplay' :{'cn':u'昨注回头昨天玩牌','sf':'sp_ybackplay'},

'cardtype_un'  :{'cn':u'牌型分布(人数)','sf':'cardtype_un'},
'cardtype_cnt' :{'cn':u'牌型分布(次数)','sf':'cardtype_cnt'},
'hourpty_un'   :{'cn':u'时段玩牌(人数)','sf':'hourpty_un'},
'hourpty_cnt'  :{'cn':u'时段玩牌(次数)','sf':'hourpty_cnt'},
'ante_property':{'cn':u'资产分布(登陆携带)','sf':'ante_property'},
'ptcurr'      :{'cn':u'牌局流通(牌局数)','sf':'pt_curr'},
'24_partyn'    :{'cn':u'时段牌局数','sf':'24_partyn'},
'ante_playnum' :{'cn':u'玩牌局数','sf':'ante_playnum'},


#牌局明细
'PARTYNUM'         : {'cn':u'局数','sf':'sp_room'},
'CHARGE'           : {'cn':u'台费','sf':'sp_room'},
'PLAYUSERNUM'      : {'cn':u'人数','sf':'sp_room'},
'USERNUM'          : {'cn':u'人次','sf':'sp_room'},
'FWIN'             : {'cn':u'赢钱','sf':'sp_room'},
'FLOSE'            : {'cn':u'输钱','sf':'sp_room'},
'FPARTYTIME'       : {'cn':u'牌局时长(分)','sf':'sp_room'},
'FPPARTYTIME'      : {'cn':u'牌局平均时长(秒)','sf':'sp_room'},
'FUSERTIME'        : {'cn':u'游戏时长(分)','sf':'sp_room'},
'FPUSERTIME'       : {'cn':u'人均时长(秒)','sf':'sp_room'},
'FPARTY_AVG'       : {'cn':u'人均玩牌局数','sf':'sp_room'},

'partynum'         : {'cn':u'局数','sf':'sp_room'},
'charge'           : {'cn':u'台费','sf':'sp_room'},
'playusernum'      : {'cn':u'人数','sf':'sp_room'},
'usernum'          : {'cn':u'人次','sf':'sp_room'},
'fwin'             : {'cn':u'赢钱','sf':'sp_room'},
'flose'            : {'cn':u'输钱','sf':'sp_room'},
'fpartytime'       : {'cn':u'牌局时长(分)','sf':'sp_room'},
'fppartytime'      : {'cn':u'牌局平均时长(秒)','sf':'sp_room'},
'fusertime'        : {'cn':u'游戏时长(分)','sf':'sp_room'},
'fpusertime'       : {'cn':u'人均时长(秒)','sf':'sp_room'},
'fparty_avg'       : {'cn':u'人均玩牌局数','sf':'sp_room'},


#底注场分析

'pu_play'          :{'cn':u'玩牌用户','sf':'pu_play'},
'pu_act'           :{'cn':u'玩牌用户','sf':'pu_act'},
'reg_play'         :{'cn':u'新增用户','sf':'reg_play'},
'reg_act'          :{'cn':u'新增用户','sf':'reg_act'},

#场次分析
'avg_lcplayusercnt': {'cn':u'玩牌人数','sf':'fp_gameparty_avg'},
'avg_lcusercnt'    : {'cn':u'玩牌人次','sf':'fp_gameparty_avg'},
'avg_partyn'       : {'cn':u'牌局数','sf':'fp_gameparty_avg'},
'avg_charge'       : {'cn':u'台费消耗','sf':'fp_gameparty_avg'},
'avg_dubrc'        : {'cn':u'破产用户数','sf':'fp_gameparty_avg'},
'avg_druptr'       : {'cn':u'破产率(%)','sf':'fp_gameparty_avg'},
'avg_dreluc'       : {'cn':u'救济人数','sf':'fp_gameparty_avg'},
'avg_dreur'        : {'cn':u'救济率(%)','sf':'fp_gameparty_avg'},
'fpname'           : {'cn':u'牌局场次','sf':'fp_gameparty_avg'},
'pn_lcplayusercnt' : {'cn':u'玩牌人数','sf':'fp_gameparty'},
'pn_lcusercnt'     : {'cn':u'玩牌人次','sf':'fp_gameparty'},
'pn_partyn'        : {'cn':u'牌局数','sf':'fp_gameparty'},
'pn_charge'        : {'cn':u'台费消耗','sf':'fp_gameparty'},
'pn_dubrc'         : {'cn':u'破产用户数','sf':'fp_gameparty'},
'pn_druptr'        : {'cn':u'破产率(%)','sf':'fp_gameparty'},
'pn_dreluc'        : {'cn':u'救济人数','sf':'fp_gameparty'},
'pn_dreur'         : {'cn':u'救济率(%)','sf':'fp_gameparty'},


'pu_retain'         : {'cn':u'玩牌用户','sf':'pu_retain'},
"p1d"               : {'cn':u'1d'},
"p2d"               : {'cn':u'2d'},
"p3d"               : {'cn':u'3d'},
"p4d"               : {'cn':u'4d'},
"p5d"               : {'cn':u'5d'},
"p6d"               : {'cn':u'6d'},
"p7d"               : {'cn':u'7d'},
"p14d"              : {'cn':u'14d'},
"p30d"              : {'cn':u'30d'},
"p60d"              : {'cn':u'60d'},
"p1dr"               : {'cn':u'+1d%'},
"p2dr"               : {'cn':u'+2d%'},
"p3dr"               : {'cn':u'+3d%'},
"p4dr"               : {'cn':u'+4d%'},
"p5dr"               : {'cn':u'+5d%'},
"p6dr"               : {'cn':u'+6d%'},
"p7dr"               : {'cn':u'+7d%'},
"p14dr"              : {'cn':u'+14d%'},
"p30dr"              : {'cn':u'+30d%'},
"p60dr"              : {'cn':u'+60d%'},


'reg_retain'         : {'cn':u'场次新增用户','sf':'reg_retain'},
"r1d"               : {'cn':u'1d'},
"r2d"               : {'cn':u'2d'},
"r3d"               : {'cn':u'3d'},
"r4d"               : {'cn':u'4d'},
"r5d"               : {'cn':u'5d'},
"r6d"               : {'cn':u'6d'},
"r7d"               : {'cn':u'7d'},
"r14d"              : {'cn':u'14d'},
"r30d"              : {'cn':u'30d'},
"r60d"              : {'cn':u'60d'},
"r1dr"               : {'cn':u'+1d%'},
"r2dr"               : {'cn':u'+2d%'},
"r3dr"               : {'cn':u'+3d%'},
"r4dr"               : {'cn':u'+4d%'},
"r5dr"               : {'cn':u'+5d%'},
"r6dr"               : {'cn':u'+6d%'},
"r7dr"               : {'cn':u'+7d%'},
"r14dr"              : {'cn':u'+14d%'},
"r30dr"              : {'cn':u'+30d%'},
"r60dr"              : {'cn':u'+60d%'},



'2dau_reflux'      :  {'cn': u'2日回流用户','sf':'not_use'},
'5dau_reflux'      :  {'cn': u'5日回流用户','sf':'not_use'},
'7dau_reflux'      :  {'cn': u'7日回流用户','sf':'not_use'},
'dau_7drfx'        :  {'cn': u'7日回流用户','sf':'not_use'},
'14dau_reflux'     :  {'cn': u'14日回流用户','sf':'not_use'},
'30dau_reflux'     :  {'cn': u'30日回流用户','sf':'not_use'},
'daunew'           :  {'cn': u'新用户','sf':'not_use'},
'dauold'           :  {'cn': u'老用户','sf':'not_use'},
'7dlogun'          :  {'cn': u'7日登陆用户数', 'class': ['user', 'base'], 'tip': u'每7天登录用户数去重'},
'30dlogun'         :  {'cn': u'30日登陆用户数', 'class': ['user', 'base'], 'tip': u'每30天登录用户数去重'},
'1daur'            :  {'cn':u'活跃1日留存','sf':'not_use'},
'1dptr'            :  {'cn':u'玩牌1日留存','sf':'not_use'},
'7daur'            :  {'cn':u'活跃7日留存','sf':'not_use'},
'7dptr'            :  {'cn':u'玩牌7日留存','sf':'not_use'},
'30daur'           :  {'cn':u'活跃30日留存','sf':'not_use'},
'30dptr'           :  {'cn':u'玩牌30日留存','sf':'not_use'},
'60daur'           :  {'cn':u'活跃60日留存','sf':'not_use'},
'60dptr'           :  {'cn':u'玩牌60日留存','sf':'not_use'},
'90daur'           :  {'cn':u'活跃90日留存','sf':'not_use'},
'90dptr'           :  {'cn':u'玩牌90日留存','sf':'not_use'},
'1dbr'             :  {'cn':u'昨注回头率','sf':'not_use'},
'3dbr'             :  {'cn':u'3注回头率','sf':'not_use'},
'7dbr'             :  {'cn':u'7注回头率','sf':'not_use'},
'14dbr'            :  {'cn':u'14注回头率','sf':'not_use'},
'30dbr'            :  {'cn':u'30注回头率','sf':'not_use'},
#游戏币监控
'dgcc'             :  {'cn':u'日游戏币消耗总数','sf':'not_use'},
'dgci'             :  {'cn':u'日游戏币发放总数','sf':'not_use'},
'dgbl'             :  {'cn':u'日游戏币流水结余'},
'userbl'           :  {'cn':u'用户结余'},
'actbl'            :  {'cn':u'活跃用户结余'},
'bankbl'           :  {'cn':u'保险箱结余'},

'dpugcc'           :  {'cn':u'日付费用户游戏币消耗'},
'dpugci'           :  {'cn':u'日付费用户游戏币发放'},
'dpugbl'           :  {'cn':u'日付费用户游戏币结余'},
'dpubygoods'       :  {'cn':u'日购买游戏币发放'},

'dnpgcc'           :  {'cn':u'非付费用户游戏币消耗'},
'dnpgci'           :  {'cn':u'日非付费用户游戏币发放'},
'dnpgbl'           :  {'cn':u'日非付费用户游戏币结余'},
'dgci_free'        :  {'cn':u'日游戏币免费发放数'},

'gamecoin_cnt'               :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_pay_cnt'           :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_cnt'          :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_free_cnt'          :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_free_cnt'     :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_user'              :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_pay_user'          :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_user'         :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_free_user'         :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_free_user'    :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_avg'               :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_pay_avg'           :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_avg'          :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_free_avg'          :   {'cn':u'游戏币流水','sf':'gamecoins'},
'gamecoin_paid_free_avg'     :   {'cn':u'游戏币流水','sf':'gamecoins'},


'sp_fage'          :   {'cn':u'回流-用户年龄','sf':'sp_fage'},
'sp_flevel'        :   {'cn':u'回流-用户等级','sf':'sp_flevel'},
'sp_fpro'          :   {'cn':u'回流-用户资产','sf':'sp_fpro'},
'sp_fparty'        :   {'cn':u'回流-用户牌局数','sf':'sp_fparty'},

'pty_ret'          :   {'cn':u'新增日用户牌局数','sf':'sp_rparty'},
'1d_pay_ret'       :   {'cn':u'新增日是否付费','sf':'sp_rpay'},
'7d_pay_ret'       :   {'cn':u'新增日是否付费','sf':'sp_rpay'},
'30d_pay_ret'      :   {'cn':u'新增日是否付费','sf':'sp_rpay'},
'1d_lgn_ret'       :   {'cn':u'新增日登陆次数','sf':'sp_rlgn'},
'7d_lgn_ret'       :   {'cn':u'新增日登陆次数','sf':'sp_rlgn'},
'30d_lgn_ret'      :   {'cn':u'新增日登陆次数','sf':'sp_rlgn'},
'1d_brp_ret'       :   {'cn':u'新增日破产次数','sf':'sp_rbrp'},
'7d_brp_ret'       :   {'cn':u'新增日破产次数','sf':'sp_rbrp'},
'30d_brp_ret'      :   {'cn':u'新增日破产次数','sf':'sp_rbrp'},
'1d_level_ret'     :   {'cn':u'新增日等级','sf':'sp_rlevel'},
'7d_level_ret'     :   {'cn':u'新增日等级','sf':'sp_rlevel'},
'30d_level_ret'    :   {'cn':u'新增日等级','sf':'sp_rlevel'},


'1d_dsurd'         :    {'cn':u'日新增留存','sf':'sp_rdsu'},
'1d_daurd'         :    {'cn':u'日活跃留存','sf':'sp_rdau'},
'7d_dsurd'         :    {'cn':u'周新增留存','sf':'sp_rwsu'},
'7d_daurd'         :    {'cn':u'日周活跃留存','sf':'sp_rwau'},
'30d_dsurd'        :    {'cn':u'月新增留存','sf':'sp_rmsu'},
'30d_daurd'        :    {'cn':u'月活跃留存','sf':'sp_rmau'},
'1d_punrd'         :    {'cn':u'日付费留存','sf':'sp_rpay'},
'1d_hpunrd'        :    {'cn':u'历史付费留存','sf':'sp_rhispay'},
'1d_dfrd'          :    {'cn':u'回流留存','sf':'sp_rreflux'},


#用户流失
'2dau_loss'         :    {'cn':u'每日用户流失(2日)','sf':'2dau_loss'},
'2dau_lossr'        :    {'cn':u'每日流失率(2日)','sf':'2dau_lossr'},
'5dau_loss'         :    {'cn':u'每日用户流失(5日)','sf':'5dau_loss'},
'5dau_lossr'        :    {'cn':u'每日流失率(5日)','sf':'5dau_lossr'},
'7dau_loss'         :    {'cn':u'每日用户流失(7日)','sf':'7dau_loss'},
'7dau_lossr'        :    {'cn':u'每日流失率(7日)','sf':'7dau_lossr'},
'14dau_loss'        :    {'cn':u'每日用户流失(14日)','sf':'14dau_loss'},
'14dau_lossr'       :    {'cn':u'每日流失率(14日)','sf':'14dau_lossr'},
'30dau_loss'        :    {'cn':u'每日用户流失(30日)','sf':'30dau_loss'},
'30dau_lossr'       :    {'cn':u'每日流失率(30日)','sf':'30dau_lossr'},

'2dau_back'        :     {'cn':u'每日回流(2日)','sf':'2dau_back'},
'5dau_back'        :     {'cn':u'每日回流(5日)','sf':'5dau_back'},
'7dau_back'        :     {'cn':u'每日回流(7日)','sf':'7dau_back'},
'14dau_back'       :     {'cn':u'每日回流(14日)','sf':'14dau_back'},
'30dau_back'       :     {'cn':u'每日回流(30日)','sf':'30dau_back'},

#流失回流分析
'bd_age'           :     {'cn':u'用户年龄','sf':'bd_age'},
'bd_level'         :     {'cn':u'用户等级','sf':'bd_level'},
'bd_property'      :     {'cn':u'用户资产','sf':'bd_property'},
'bd_party'         :     {'cn':u'用户牌局','sf':'bd_party'},

'ed_lcnt'           :     {'cn':u'付费次数','sf':'ed_lcnt'},
'ed_lip'            :     {'cn':u'付费额度','sf':'ed_lip'},
'ed_rupt'           :     {'cn':u'破产次数','sf':'ed_rupt'},
'ed_level'          :     {'cn':u'用户等级','sf':'ed_level'},
'ed_lup'            :     {'cn':u'用户资产','sf':'ed_lup'},
'dsu_loss'          :     {'cn':u'新增用户','sf':'loss_ana'},
'dpu_loss'          :     {'cn':u'付费用户','sf':'dpu_loss'},

#游戏习惯
'dlogun_avg'          :     {'cn':u'平均游戏次数','sf':'not_use'},
'7dlogun_avg'         :     {'cn':u'7日平均游戏次数','sf':'not_use'},
'30dlogun_avg'        :     {'cn':u'30日平均游戏次数','sf':'not_use'},
'dlogun_avgt'         :     {'cn':u'平均在线时长','sf':'not_use'},
'7dlogun_avgt'        :     {'cn':u'7日平均在线时长','sf':'not_use'},
'30dlogun_avgt'       :     {'cn':u'30日平均在线时长','sf':'not_use'},

'dau_ag7d'        :     {'cn':u'活跃周平均游戏天数','sf':'not_use'},
'dau_ag30d'       :     {'cn':u'活跃月平均游戏天数','sf':'not_use'},
'dru_ag7d'        :     {'cn':u'新增周平均游戏天数','sf':'not_use'},
'dru_ag30d'       :     {'cn':u'新增月平均游戏天数','sf':'not_use'},
'dpu_ag7d'        :     {'cn':u'付费周平均游戏天数','sf':'not_use'},
'dpu_ag30d'       :     {'cn':u'付费月平均游戏天数','sf':'not_use'},
'dbu_ag7d'        :     {'cn':u'比赛周平均游戏天数','sf':'not_use'},
'dbu_ag30d'       :     {'cn':u'比赛月平均游戏天数','sf':'not_use'},

'playcnt'         :     {'cn':u'所有用户玩牌时长','sf':'sp_playt'},
'payplaycnt'      :     {'cn':u'付费用户玩牌时长','sf':'sp_playt'},

'24h_pun'         :     {'cn':u'玩牌人数','sf':'sp_24h'},
'24h_partyn'      :     {'cn':u'牌局数','sf':'sp_24h'},
'ulogincnt'       :     {'cn':u'登录人数','sf':'sp_24h'},
'slogincnt'       :     {'cn':u'登录次数','sf':'sp_24h'},

#用户破产
'drupt_pur'           :     {'cn':u'破产付费率','sf':'not_use'},
'dreluc'              :     {'cn':u'救济用户数','sf':'not_use'},
'dreur'               :     {'cn':u'救济率','sf':'not_use'},
'dbrc'                :     {'cn':u'破产次数','sf':'not_use'},
'dsucc'               :     {'cn':u'救济次数','sf':'not_use'},
'dabrc'               :     {'cn':u'人均破产次数','sf':'not_use'},
'dareluc'             :     {'cn':u'人均救济次数','sf':'not_use'},
'br_1br'              :     {'cn':u'1破回头率','sf':'not_use'},
'br_2br'              :     {'cn':u'2破回头率','sf':'not_use'},
'br_3br'              :     {'cn':u'3破回头率','sf':'not_use'},
'br_4br'              :     {'cn':u'4破回头率','sf':'not_use'},
'br_5br'              :     {'cn':u'5破回头率','sf':'not_use'},
'br_6br'              :     {'cn':u'6破回头率','sf':'not_use'},
'br_7br'              :     {'cn':u'7破回头率','sf':'not_use'},
'br_14br'             :     {'cn':u'14破回头率','sf':'not_use'},
'br_30br'             :     {'cn':u'30破回头率','sf':'not_use'},
'br_1bu'              :     {'cn':u'1破回头率','sf':'not_use'},
'br_2bu'              :     {'cn':u'2破回头率','sf':'not_use'},
'br_3bu'              :     {'cn':u'3破回头率','sf':'not_use'},
'br_4bu'              :     {'cn':u'4破回头率','sf':'not_use'},
'br_5bu'              :     {'cn':u'5破回头率','sf':'not_use'},
'br_6bu'              :     {'cn':u'6破回头率','sf':'not_use'},
'br_7bu'              :     {'cn':u'7破回头率','sf':'not_use'},
'br_14bu'             :     {'cn':u'14破回头率','sf':'not_use'},
'br_30bu'             :     {'cn':u'30破回头率','sf':'not_use'},
'brupt_partyuser'     :     {'cn':u'场次分布','sf':'brupt_partyuser'},
'brupt_pouruser'      :     {'cn':u'底注分布','sf':'brupt_pouruser'},
'brupt_scene'         :     {'cn':u'场景分布','sf':'brupt_scene'},
'burpt_level'         :     {'cn':u'破产用户数','sf':'burpt_level'},
'brupt_dau'           :     {'cn':u'活跃用户','sf':'brupt_dau'},
'brupt_pay'           :     {'cn':u'付费用户','sf':'brupt_pay'},
'brupt_paid'          :     {'cn':u'历史付费用户','sf':'brupt_paid'},
'brupt_dsu'           :     {'cn':u'新增用户','sf':'brupt_dsu'},
'dsucc_dsu'           :     {'cn':u'救济次数','sf':'dsucc_dsu'},
'drupt_bal'           :     {'cn':u'破产用户资产分布','sf':'drupt_bal'},

#机型分布
'reg_mtype'           :     {'cn':u'机型','sf':'device_type'},
'act_mtype'           :     {'cn':u'机型','sf':'device_type'},
'pay_mtype'           :     {'cn':u'机型','sf':'device_type'},
'reg_mpixel'          :     {'cn':u'分辨率','sf':'mpixel_type'},
'act_mpixel'          :     {'cn':u'分辨率','sf':'mpixel_type'},
'pay_mpixel'          :     {'cn':u'分辨率','sf':'mpixel_type'},
'reg_mos'             :     {'cn':u'操作系统','sf':'mos_type'},
'act_mos'             :     {'cn':u'操作系统','sf':'mos_type'},
'pay_mos'             :     {'cn':u'操作系统','sf':'mos_type'},
'reg_mnetwork'        :     {'cn':u'联网方式','sf':'mnetwork_type'},
'act_mnetwork'        :     {'cn':u'联网方式','sf':'mnetwork_type'},
'pay_mnetwork'        :     {'cn':u'联网方式','sf':'mnetwork_type'},
'reg_moperator'       :     {'cn':u'运营商','sf':'moperator_type'},
'act_moperator'       :     {'cn':u'运营商','sf':'moperator_type'},
'pay_moperator'       :     {'cn':u'运营商','sf':'moperator_type'},

#付费习惯
'dsu_punm'            :     {'cn':u'付费用户数','sf':'dsu_ip'},
'dsu_income'          :     {'cn':u'充值总额(USD)','sf':'dsu_ip'},
'dsu_fpunm'           :     {'cn':u'新增付费用户数','sf':'dsu_ip'},
'dsu_fincome'         :     {'cn':u'首付充值总额(USD)','sf':'dsu_ip'},
'p_income'            :     {'cn':u'人均充值额','sf':'dsu_ip'},
'fp_income'           :     {'cn':u'首付人均充值额','sf':'dsu_ip'},
'dsu_apunm'           :     {'cn':u'当天付费用户数比例','sf':'dsu_ip'},
'dsu_afpunm'          :     {'cn':u'当天首付用户数比例','sf':'dsu_ip'},

'all_pay_unm'           :     {'cn':u'付费人数','sf':'pay_unm_ver'},
'all_pay_nm'            :     {'cn':u'付费额度','sf':'pay_unm_ver'},
'all_pay_cnt'           :     {'cn':u'付费次数','sf':'pay_unm_ver'},
'fpay_pay_unm'          :     {'cn':u'付费人数','sf':'pay_unm_ver'},
'fpay_pay_unm'          :     {'cn':u'付费额度','sf':'pay_unm_ver'},
'fpay_pay_unm'          :     {'cn':u'付费次数','sf':'pay_unm_ver'},

'ver_all_pay_unm'           :     {'cn':u'付费人数','sf':'pay_unm_ver'},
'ver_all_pay_nm'            :     {'cn':u'付费额度','sf':'pay_unm_ver'},
'ver_all_pay_cnt'           :     {'cn':u'付费次数','sf':'pay_unm_ver'},
'ver_fpay_pay_unm'          :     {'cn':u'付费人数','sf':'pay_unm_ver'},
'ver_fpay_pay_cnt'          :     {'cn':u'付费额度','sf':'pay_unm_ver'},
'ver_fpay_pay_nm'           :     {'cn':u'付费次数','sf':'pay_unm_ver'},

'coins_num'                 :     {'cn':u'订单面额','sf':'coins_num'},
'nuser_dpcnt'               :     {'cn':u'付费次数','sf':'nuser_dpcnt'},
'nuser_dpa'                 :     {'cn':u'付费额度','sf':'nuser_dpa'},
'gappu'                     :     {'cn':u'付费间隔','sf':'gappu'},
'24h_ips'                   :     {'cn':u'付费收入','sf':'24h_ips'},
'24h_pus'                    :     {'cn':u'付费人数','sf':'24h_pus'},
'7dpstat'                   :     {'cn':u'付费天(7天)','sf':'7dpstat'},
'14dpstat'                  :     {'cn':u'付费天(14天)','sf':'14dpstat'},
'30dpstat'                  :     {'cn':u'付费天(30天)','sf':'30dpstat'},

'regpay_days'                  :     {'cn':u'用户付费年龄','sf':'regpay_days'},
'entrance_pay'                 :     {'cn':u'付费用户账号','sf':'entrance_pay'},
'pay_unum'                     :     {'cn':u'付费用户数','sf':'pay_product'},
'income'                       :     {'cn':u'付费次数','sf':'pay_product'},
'pay_cnt'                      :     {'cn':u'付费额度','sf':'pay_product'},
'pay_acnt'                     :     {'cn':u'人均付费次数','sf':'pay_product'},
'aincome'                      :     {'cn':u'人均付费额度','sf':'pay_product'},

#付费场景
'ocr'                          :     {'cn':u'订单完成率','sf':'not_use'},
'ordercnt'                     :     {'cn':u'下单数','sf':'not_use'},
'orderun'                      :     {'cn':u'下单用户数','sf':'not_use'},
'order_ar'                     :     {'cn':u'活跃下单率','sf':'not_use'},
'bankip'                       :     {'cn':u'破产用户收入','sf':'not_use'},
'bankpu'                       :     {'cn':u'破产付费用户','sf':'not_use'},

'ps_ocr'                        :     {'cn':u'付费场景','sf':'ps_ocr'},
'pgp_ocr'                       :     {'cn':u'付费场次','sf':'pgp_ocr'},
'pmn_ocr'                       :     {'cn':u'付费渠道','sf':'pmn_ocr'},


'ps_income'                     :     {'cn':u'收入','sf':'ps_income'},
'ps_ordercnt'                   :     {'cn':u'总下单数','sf':'ps_income'},
'ps_orderun'                    :     {'cn':u'总下单用户数','sf':'ps_income'},
'ps_pcnt'                       :     {'cn':u'付费用户','sf':'ps_income'},
'ps_pu'                         :     {'cn':u'付费次数','sf':'ps_income'},

'pgp_income'                     :     {'cn':u'收入','sf':'pgp_income'},
'pgp_ordercnt'                   :     {'cn':u'总下单数','sf':'pgp_income'},
'pgp_orderun'                    :     {'cn':u'总下单用户数','sf':'pgp_income'},
'pgp_pcnt'                       :     {'cn':u'付费用户','sf':'pgp_income'},
'pgp_pu'                         :     {'cn':u'付费次数','sf':'pgp_income'},

'pmn_income'                     :     {'cn':u'收入','sf':'pmn_income'},
'pmn_ordercnt'                   :     {'cn':u'总下单数','sf':'pmn_income'},
'pmn_orderun'                    :     {'cn':u'总下单用户数','sf':'pmn_income'},
'pmn_pcnt'                       :     {'cn':u'付费用户','sf':'pmn_income'},
'pmn_pu'                         :     {'cn':u'付费次数','sf':'pmn_income'},

'sorder'                         :     {'cn':u'总下单用户数','sf':'sorder'},
'fuser'                          :     {'cn':u'付费用户','sf':'sorder'},
'fpay'                           :     {'cn':u'付费次数','sf':'sorder'},

'24h_cumpu'                      :     {'cn':u'付费用户数','sf':'24h_cu'},
'24h_cumip'                      :     {'cn':u'付费额度','sf':'24h_cuip'},
'24h_cumpcnt'                    :     {'cn':u'付费次数','sf':'24h_cunt'},

'fuid'                           :     {'cn':u'用户id','sf':'top100_user'},
'fplatform_uid'                  :     {'cn':u'平台id','sf':'top100_user'},
'fgpname'                        :     {'cn':u'游戏平台','sf':'top100_user'},
'fpaycnt'                        :     {'cn':u'充值次数','sf':'top100_user'},
'tdip'                           :     {'cn':u'充值金额','sf':'top100_user'},
'flognum'                        :     {'cn':u'登录次数','sf':'top100_user'},
'fplaynum'                       :     {'cn':u'玩牌局数','sf':'top100_user'},
'fgc_in'                         :     {'cn':u'游戏币发放','sf':'top100_user'},
'fgc_out'                        :     {'cn':u'游戏币消耗','sf':'top100_user'},
'fnote'                          :     {'cn':u'备注','sf':'top100_user'},
'foperate'                       :     {'cn':u'操作','sf':'top100_user'},

'ftop_payun'                     :     {'cn':u'充值用户数','sf':'top100_day'},
'ftop_playun'                    :     {'cn':u'玩牌人数','sf':'top100_day'},
'ftopgc_in'                      :     {'cn':u'发放游戏币','sf':'top100_day'},
'ftopgc_out'                     :     {'cn':u'消耗游戏币','sf':'top100_day'},
'top_dip'                        :     {'cn':u'充值金额','sf':'top100_day'},
'fpayun'                         :     {'cn':u'总充值用户数','sf':'top100_day'},
'stdip'                          :     {'cn':u'总充值金额','sf':'top100_day'},
'tdipr'                          :     {'cn':u'top100充值用户占比','sf':'top100_day'},
'tpayur'                         :     {'cn':u'top100充值金额占比','sf':'top100_day'},

'fsk'                            :     {'cn':u'编号','sf':''},
'fname'                          :     {'cn':u'显示名称','sf':''},
'fis_pay'                        :     {'cn':u'支付','sf':''},
'fis_gambling'                   :     {'cn':u'牌局','sf':''},
'fis_prop'                       :     {'cn':u'道具','sf':''},
'fis_box'                        :     {'cn':u'保险箱','sf':''},
'fis_taifei'                     :     {'cn':u'台费','sf':''},
'fis_circulate'                  :     {'cn':u'流通','sf':''},
'ftype'                          :     {'cn':u'编号','sf':''},
'remarker'                       :     {'cn':u'添加人','sf':''},
'description'                    :     {'cn':u'描述','sf':''},
'fevent'                         :     {'cn':u'备注','sf':''},
'frule_id'                       :     {'cn':u'编号','sf':''},
'flangtypename'                  :     {'cn':u'语言','sf':''},


#日志监控
'api_name_en'                         :     {'cn':u'接口名称(英文)','sf':'log_summary'},
'api_name_zh'                         :     {'cn':u'接口名称(中文)','sf':'log_summary'},
'total_log_num'                       :     {'cn':u'总条数','sf':'log_tread'},
'right_log_num'                       :     {'cn':u'正确条数','sf':'log_tread'},
'wrong_log_num'                       :     {'cn':u'错误条数','sf':'log_tread'},

'dtotal_log_num'                       :     {'cn':u'总条数','sf':'log_detail'},
'dright_log_num'                       :     {'cn':u'正确条数','sf':'log_detail'},
'dwrong_log_num'                       :     {'cn':u'错误条数','sf':'log_detail'},

# 活动事件
'actu_cnt'                             :     {'cn':u'参与人数','sf':'act_summary'},
'actu_num'                             :     {'cn':u'参与次数','sf':'act_summary'},
'act_avg_cnt'                          :     {'cn':u'人均次数','sf':'act_summary'},
'act_pr'                               :     {'cn':u'参与率%','sf':'act_summary'},
'act_pay_unm'                          :     {'cn':u'参与人数(付费用户)','sf':'act_summary'},
'act_reg_unm'                          :     {'cn':u'参与人数(新增用户)','sf':'act_summary'},
'act_fpay_unm'                         :     {'cn':u'参与人数(首付用户)','sf':'act_summary'},
'act_total_income'                     :     {'cn':u'付费总额','sf':'act_summary'},
'farg_name'                            :     {'cn':u'参数ID'},
'fdis_name'                            :     {'cn':u'显示名称'},

'act_cost'                             :     {'cn':u'活动消耗','sf':'act_cost'},
'24h_aucnt'                            :     {'cn':u'分时段参与次数','sf':'24h_act'},
'24h_aunum'                            :     {'cn':u'分时段参与人数','sf':'24h_act'},
'act_rcnt'                             :     {'cn':u'条件达成(次数)','sf':'act_rcnt'},
'act_rnum'                             :     {'cn':u'条件达成(人数)','sf':'act_rcnt'},
'act_retain'                           :     {'cn':u'活动人数','sf':'act_retain'},
'pay_retain'                           :     {'cn':u'活动人数','sf':'pay_retain'},
'userpay_retain'                       :     {'cn':u'活动人数','sf':'userpay_retain'},

'fact_id'                              :     {'cn':u'活动id','sf':'act_outline'},
'fact_name'                            :     {'cn':u'活动名称','sf':'act_outline'},
'fsdate'                               :     {'cn':u'开始日期','sf':'act_outline'},
'fedate'                               :     {'cn':u'结束日期','sf':'act_outline'},
'fdesc'                                :     {'cn':u'描述','sf':'act_outline'},
'ac_cnt'                               :     {'cn':u'参与次数','sf':'act_outline'},
'ac_num'                               :     {'cn':u'参与人数','sf':'act_outline'},
'avg_cnt'                              :     {'cn':u'人均次数','sf':'act_outline'},
'pr'                                   :     {'cn':u'参与率%','sf':'act_outline'},
'ac_pay'                               :     {'cn':u'参与人数(付费用户)','sf':'act_outline'},
'ac_dsu'                               :     {'cn':u'参与人数(新增用户)','sf':'act_outline'},
'ac_fpay'                              :     {'cn':u'参与人数(首付用户)','sf':'act_outline'},
'act_total_income'                     :     {'cn':u'付费总额','sf':'act_outline'},

'pt_qj'            :{'cn':u'局数区间','sf':'rt_dsu_party'},
'rt_dsu'           :{'cn':u'新增用户','sf':'rt_dsu_party'},
'pay_ret'          :{'cn':u'付费用户数','sf':'pay_ret'},
'+1dr'             :{'cn':u'+1d%'},
'+2dr'             :{'cn':u'+2d%'},
'+3dr'             :{'cn':u'+3d%'},
'+4dr'             :{'cn':u'+4d%'},
'+5dr'             :{'cn':u'+5d%'},
'+6dr'             :{'cn':u'+6d%'},
'+7dr'             :{'cn':u'+7d%'},
'+14dr'            :{'cn':u'+14d%'},
'+30dr'            :{'cn':u'+30d%'},
'+60dr'            :{'cn':u'+60d%'},

'1dr'              :{'cn':u'+1d%'},
'2dr'              :{'cn':u'+2d%'},
'3dr'              :{'cn':u'+3d%'},
'4dr'              :{'cn':u'+4d%'},
'5dr'              :{'cn':u'+5d%'},
'6dr'              :{'cn':u'+6d%'},
'7dr'              :{'cn':u'+7d%'},
'14dr'             :{'cn':u'+14d%'},
'30dr'             :{'cn':u'+30d%'},
'60dr'             :{'cn':u'+60d%'},

'1d'               :{'cn':u'+1d'},
'2d'               :{'cn':u'+2d'},
'3d'               :{'cn':u'+3d'},
'4d'               :{'cn':u'+4d'},
'5d'               :{'cn':u'+5d'},
'6d'               :{'cn':u'+6d'},
'7d'               :{'cn':u'+7d'},
'14d'              :{'cn':u'+14d'},
'30d'              :{'cn':u'+30d'},
'60d'              :{'cn':u'+60d'},

'v_paycnt'         :{'cn':u'付费次数','sf':'virtual_top'},
'v_dip'            :{'cn':u'付费金额','sf':'virtual_top'},
'v_pcn'            :{'cn':u'购买数量','sf':'virtual_top'},
'v_playnum'        :{'cn':u'玩牌局数','sf':'virtual_top'},
'v_gc_in'          :{'cn':u'发放','sf':'virtual_top'},
'v_gc_out'         :{'cn':u'消耗','sf':'virtual_top'},

'rank'             :{'cn':u'排名'},
'fplatform_uid'    :{'cn':u'平台用户ID'},
'fgpname'          :{'cn':u'游戏-平台'},


'date'             :{'cn':u'日期'},
'io_way'           :{'cn':u'发放消耗'},
'gcname'           :{'cn':u'消费点名称'},
'propname'         :{'cn':u'道具名称'},
'cs_cnt'           :{'cn':u'消费次数'},
'cs_num'           :{'cn':u'消费数量'},
'pay_way'          :{'cn':u'支付方式'},
'money'            :{'cn':u'充值金额'},
'currency'         :{'cn':u'原币类型'},
'goods'            :{'cn':u'购买物品'},
'scene'            :{'cn':u'支付场景'},
'top_uid_pays'     :{'cn':u'充值曲线','sf':'top_uid_pays'},


'top_uid_pay'      :{'cn':u'用户每日充值金额','sf':'uid_pay_day'},
'foperate'         :{'cn':u'操作'},


'rp_list'           :{'cn':u'日报模板列表', 'sf':'rp_list'},

'fdate'             :{'cn':u'日期'},
'gpv'               :{'cn':u'游戏应用'},
'bs_fname'          :{'cn':u'比赛房间'},
'bs_fpname'         :{'cn':u'比赛场'},
'bs_fsubname'       :{'cn':u'具体赛事'},

'fet_id'            :{'cn':u'事件id'},
'fet_name'          :{'cn':u'事件名称'},
'fgamename'         :{'cn':u'应用'},
'ecnt'              :{'cn':u'事件次数','sf':'event_detail'},
'eun'               :{'cn':u'事件用户数','sf':'event_detail'},
'reun'              :{'cn':u'事件人数占活跃比'},

#事件列表详细
'fargcnt'           :{'cn':u'次数','sf':'event_act_detail'},
'fusercnt'          :{'cn':u'人数','sf':'event_act_detail'},
'fargvalue_sum'     :{'cn':u'汇总值','sf':'event_act_detail'},
'fargvalue'         :{'cn':u'操作值','sf':'event_click_detail'},
'efargcnt'          :{'cn':u'次数','sf':'event_click_detail'},
'efusercnt'         :{'cn':u'人数','sf':'event_click_detail'},

#每日经济
'enc_outline'          :{'cn':u'金流自定义','sf':'day_enc_outline'},
'enc_detail'           :{'cn':u'金流自定义','sf':'day_enc_detail'},


#博雅币监控
'dgcc_by'             :  {'cn':u'日博雅币消耗总数','sf':'bycoins_detail'},
'dgci_by'             :  {'cn':u'日博雅币发放总数','sf':'bycoins_detail'},
'dgbl_by'             :  {'cn':u'日博雅币流水结余','sf':'bycoins_detail'},
'userbl_by'           :  {'cn':u'日博雅币用户结余','sf':'bycoins_detail'},


'dgccpu_by'             :  {'cn':u'日博雅币付费消耗总数','sf':'bycoins_detail_pu'},
'dgcipu_by'             :  {'cn':u'日博雅币付费发放总数','sf':'bycoins_detail_pu'},
'dgblpu_by'             :  {'cn':u'日博雅币付费流水结余','sf':'bycoins_detail_pu'},
'userblpu_by'           :  {'cn':u'日博雅币付费用户结余','sf':'bycoins_detail_pu'},

'dgccnp_by'             :  {'cn':u'日博雅币非付费消耗总数','sf':'bycoins_detail_np'},
'dgcinp_by'             :  {'cn':u'日博雅币非付费发放总数','sf':'bycoins_detail_np'},
'dgblnp_by'             :  {'cn':u'日博雅币非付费流水结余','sf':'bycoins_detail_np'},
'userblnp_by'           :  {'cn':u'日博雅币非付费用户结余','sf':'bycoins_detail_np'},

'bycoin_cnt'               :   {'cn':u'博雅币流水','sf':'bycoins'},
'bycoin_num'               :   {'cn':u'博雅币流水','sf':'bycoins'},
'bycoin_user'              :   {'cn':u'博雅币流水','sf':'bycoins'},
'bycoin_avg'               :   {'cn':u'博雅币流水','sf':'bycoins'},

'fplatformname'            :   {'cn':u'平台','sf':'not_use'},

#报警配置
'fopera_at'                :{'cn':u'操作时间','sf':'not_use'},
'fopera_name'              :{'cn':u'操作人','sf':'not_use'},
'fopera_detailed'          :{'cn':u'操作','sf':'not_use'},
'fdisplay_name'            :{'cn':u'用户名','sf':'not_use'},

# 礼物
'gf_num':  {'cn':u'礼物数量','sf':'gift_finace','group_by':'fname'},
'gf_unum':  {'cn':u'礼物人数','sf':'gift_finace','group_by':'fname'},

# 游戏币类型
"coin_type":{'cn':u'币种类型','sf':'coin_type'},
'fhallname' : {'cn':u'大厅','sf':'1'},
'fversionname' : {'cn':u'应用包','sf':'1'},
'fterminaltypename' : {'cn':u'终端','sf':'1'},
'fcreate_at' : {'cn':u'创建时间','sf':'1'},

# 实时收入
'rt_dpcnt_all':{'cn':u'付费次数','sf':'rt_income'},
'rt_dpu_all':{'cn':u'付费用户数','sf':'rt_income'},
'rt_dip_all':{'cn':u'付费总额','sf':'rt_income'},


'rt_incomecnt':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomecnt':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomecnt':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_incomepu':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomepu':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomepu':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_incomeip':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomeip':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomeip':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},


'rt_incomecnt_acc':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomecnt_acc':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomecnt_acc':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_incomepu_acc':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomepu_acc':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomepu_acc':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_incomeip_acc':{'cn':today,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_1incomeip_acc':{'cn':yesterday,'sf':'rt_income_new','column_list':[i for i in range(24)]},
'rt_7incomeip_acc':{'cn':lastweekday,'sf':'rt_income_new','column_list':[i for i in range(24)]},

# 实时概况
"rt_dau":{'cn':u'日活跃用户','sf':''},
"rt_dgcc":{'cn':u'日游戏币消耗总数','sf':''},
"rt_dgci":{'cn':u'日游戏币发放总数','sf':''},
"rt_dsu":{'cn':u'日新增用户','sf':'rt_dsu_party'},
"rt_pun":{'cn':u'玩牌人数','sf':''},

"rt_dau_hour":{'cn':u'日活跃用户','sf':'','column_list':[i for i in range(24)]},
"rt_dgcc_hour":{'cn':u'日游戏币消耗总数','sf':'','column_list':[i for i in range(24)]},
"rt_dgci_hour":{'cn':u'日游戏币发放总数','sf':'','column_list':[i for i in range(24)]},
"rt_dsu_hour":{'cn':u'日新增用户','sf':'','column_list':[i for i in range(24)]},
"rt_pun_hour":{'cn':u'玩牌人数','sf':'','column_list':[i for i in range(24)]},

# 实时牌局
"rt_ptunum":{'cn':u'玩牌人数','sf':'rt_gameparty',
             'column_list':["%s:%s" % (str(i).zfill(2),str(j).zfill(2)) for i in range(24) for j in range(0,60,5)],
             'group_by':'title'},
"rt_ptnum":{'cn':u'牌局数','sf':'rt_gameparty',
             'column_list':["%s:%s" % (str(i).zfill(2),str(j).zfill(2)) for i in range(24) for j in range(0,60,5)],
             'group_by':'title'},
"rt_ptrunum":{'cn':u'玩牌人数','sf':'rt_gameparty_room',
             'column_list':["%s:%s" % (str(i).zfill(2),str(j).zfill(2)) for i in range(24) for j in range(0,60,5)],
             'group_by':'title'},
"rt_ptrnum":{'cn':u'牌局数','sf':'rt_gameparty_room',
             'column_list':["%s:%s" % (str(i).zfill(2),str(j).zfill(2)) for i in range(24) for j in range(0,60,5)],
             'group_by':'title'},

#在线在玩
'zz_ou':{'cn':u'在线实时','sf':'zai_xian',
         'column_list': ["%s:%s" % (str(i).zfill(2), str(j).zfill(2)) for i in range(24) for j in range(0, 60, 5)],
        'group_by':'fdate'
         },
'zz_opu':{'cn':u'在玩实时','sf':'zai_wan',
         'column_list': ["%s:%s" % (str(i).zfill(2), str(j).zfill(2)) for i in range(24) for j in range(0, 60, 5)],
        'group_by':'fdate'
         },
'zz_out':{
    'cn':u'在线实时','sf':'zai_baset'
},
'zz_oput':{
    'cn':u'在玩实时','sf':'zai_baset'
},

'zz_omax':{
    'cn':u'在线峰值','sf':'zai_day','count_all':True,'count_avg':True
},
'zz_oavg':{
    'cn':u'在线均值','sf':'zai_day'
},
'zz_oper':{
    'cn':u'ACU/PCU','sf':'zai_day'
},

# 道具分析

"pp_inum":{
    'cn':u'发放数量','sf':'props','first_column':{'name':'type','displayName':u'道具'},'percent':False
    },
"pp_iunum":{
    'cn':u'发放人量','sf':'props','first_column':{'name':'type','displayName':u'道具'},'percent':False
    },
"pp_onum":{
    'cn':u'消耗数量','sf':'props','first_column':{'name':'type','displayName':u'道具'},'percent':False
    },
"pp_ounum":{
    'cn':u'消耗人量','sf':'props','first_column':{'name':'type','displayName':u'道具'},'percent':False
    },

"pp_type":{
    'cn':u'查看','sf':'props','first_column':{'name':'type','displayName':u'道具'},'percent':False,'no_plus':True,
    },


"pp_dinum":{
    'cn':u'数量','sf':'props','first_column':{'name':'fdate','displayName':u'日期'},'ccc':'fdate'
    },
"pp_diunum":{
    'cn':u'人量','sf':'props','first_column':{'name':'fdate','displayName':u'日期'},'ccc':'fdate'
    },

"pp_donum":{
    'cn':u'数量','sf':'props','first_column':{'name':'fdate','displayName':u'日期'},'ccc':'fdate'
    },
"pp_dounum":{
    'cn':u'人量','sf':'props','first_column':{'name':'fdate','displayName':u'日期'},'ccc':'fdate'
    },
"pp_diway":{
    'cn':u'人量','sf':'props_way_in'
    },
"pp_doway":{
    'cn':u'人量','sf':'props_way_out'
    },
"pp_diwayt":{
    'cn':u'人量','sf':'props_way_in','group_by':'fname','ccc':'fdate','count_all':True,'count_avg':True
    },
"pp_dowayt":{
    'cn':u'人量','sf':'props_way_out','group_by':'fname','ccc':'fdate','count_all':True,'count_avg':True
    },

"pp_disub":{
    'cn':u'人量','sf':'props_sub_in'
    },
"pp_dosub":{
    'cn':u'人量','sf':'props_sub_out'
    },
"pp_dosubt":{
    'cn':u'人量','sf':'props_sub_out','group_by':'fname','ccc':'fdate','count_all':True,'count_avg':True
    },
"pp_disubt":{
    'cn':u'人量','sf':'props_sub_in','group_by':'fname','ccc':'fdate','count_all':True,'count_avg':True
    },

# 资产分布
"zc_active":{'cn':u'活跃','sf':'zc_jinbi','ccc':'fdate','group_by':'fname','chart_noeffect':True},
"zc_bankrput":{'cn':u'破产','sf':'zc_jinbi','ccc':'fdate','group_by':'fname','chart_noeffect':True},
"zc_pay":{'cn':u'付费','sf':'zc_jinbi','ccc':'fdate','group_by':'fname','chart_noeffect':True},
"zc_bank":{'cn':u'活跃(保险箱)','sf':'zc_jinbi','ccc':'fdate','group_by':'fname','chart_noeffect':True},
"zc_act_bank":{'cn':u'活跃(携带+保险箱)','sf':'zc_jinbi','ccc':'fdate','group_by':'fname','chart_noeffect':True},
"zc_act_by":{'cn':u'活跃(博雅币)','sf':'zc_jinbi_thin','ccc':'fdate','group_by':'fname','chart_noeffect':True},

# 牌局日报
'fdis_name':{'cn':u'房间'},
'fsubname':{'cn':u'房间'},
'fante':{'cn':u'底注'},
'fplayuser_num':{'cn':u'玩牌人数','sf':'board_daily'},
'fbankuser_num':{'cn':u'破产人数','sf':'board_daily'},
'fbankuser_cnt':{'cn':u'破产人次','sf':'board_daily'},
'board_bur':{'cn':u'破产率(%)','sf':'board_daily'},
'board_drupt_pur':{'cn':u'破产付费率','sf':'board_daily'},
'drupt_pur_10':{'cn':u'破产付费率10min(%)','sf':'board_daily'},
'fparty_num':{'cn':u'牌局数','sf':'board_daily'},
'fwinplayer_cnt':{'cn':u'赢牌人次','sf':'board_daily'},
'floseplayer_cnt':{'cn':u'输牌人次','sf':'board_daily'},
'fbankparty_num':{'cn':u'破产局数','sf':'board_daily'},
'partybur':{'cn':u'牌局破产率(%)','sf':'board_daily'},
'fwingc_sum':{'cn':u'牌局总赢','sf':'board_daily'},
'flosegc_sum':{'cn':u'牌局总输','sf':'board_daily'},
'fwingc_avg':{'cn':u'平均每局赢','sf':'board_daily'},
'flosegc_avg':{'cn':u'平均每局输','sf':'board_daily'},
'fcharge':{'cn':u'台费','sf':'board_daily'},
'fmultiple_avg':{'cn':u'平均倍数','sf':'board_daily'},
'f1bankrupt_num':{'cn':u'一人破产局','sf':'board_daily'},
'f2bankrupt_num':{'cn':u'二人破产局','sf':'board_daily'},
'frb_num':{'cn':u'机器人个数','sf':'board_daily'},
'fremain_coins':{'cn':u'机器人总金币结余','sf':'board_daily'},
'fwin_coins':{'cn':u'机器人总赢金币','sf':'board_daily'},
'flost_coins':{'cn':u'机器人总输金币','sf':'board_daily'},
'frobots_party_num':{'cn':u'机器人牌局数','sf':'board_daily'},
'frobots_win_rate':{'cn':u'机器人胜率(%)','sf':'board_daily'},

#应用统计--通道监控
'args':{'cn':""},
'pay_money':{'cn':u'付费金额','sf':'pay_alarm'},
'pay_money_avg':{'cn':u'付费金额','sf':'pay_alarm'},
'pay_money_hb':{'cn':u'付费金额','sf':'pay_alarm'},
'pay_money_tb':{'cn':u'付费金额','sf':'pay_alarm'},
'pay_usercnt':{'cn':u'付费次数','sf':'pay_alarm'},
'pay_ordercnt':{'cn':u'下单数','sf':'pay_alarm'},
'pay_ordercnt_avg':{'cn':u'下单数','sf':'pay_alarm'},
'pay_ordercnt_hb':{'cn':u'下单数','sf':'pay_alarm'},
'pay_ordercnt_tb':{'cn':u'下单数','sf':'pay_alarm'},
'pay_ocr':{'cn':u'订单完成率','sf':'pay_alarm'},
'pay_ocr_avg':{'cn':u'订单完成率','sf':'pay_alarm'},
'pay_ocr_hb':{'cn':u'订单完成率','sf':'pay_alarm'},
'pay_ocr_tb':{'cn':u'订单完成率','sf':'pay_alarm'},
'fpay_kind':{'cn':u'支付类型'},
'fm_name':{'cn':u'支付方式'},
'fcountry':{'cn':u'国家'},
'fprovince':{'cn':u'省份'},
'daopu':{'cn':u'平均在玩'},
'daou':{'cn':u'日平均在线'},
'mau':{'cn':u'月活跃'},
'msu':{'cn':u'月新增'},
'mpun':{'cn':u'月玩牌用户数'},
'mpu':{'cn':u'月付费用户数'},
'mip':{'cn':u'月付费金额'},
'maou':{'cn':u'月平均在线'},
'maopu':{'cn':u'月平均在玩'},
'arppu':{'cn':u'ARPPU'},
'darppu':{'cn':u'日ARPPU'},
'marppu':{'cn':u'月ARPPU'},
'mau_da':{'cn':u'日均活跃用户数'},
'msu_da':{'cn':u'日均新增用户数'},
'mpun_da':{'cn':u'日均玩牌用户数'},
'mpu_da':{'cn':u'日均付费用户数'},
'mip_da':{'cn':u'日均付费金额'},
'maopu_da':{'cn':u'日均在玩均值'},
'maou_da':{'cn':u'日均在线均值'},
'pur_da':{'cn':u'日均付费渗透率'},
'arppu_da':{'cn':u'日均ARPPU'},
'mpur':{'cn':u'月付费率'},
'dpur':{'cn':u'日付费率'},


# 地区分布
'cy_dsu':{'cn':u'日新增用户','sf':'area_cy'},
'cy_dau':{'cn':u'日活跃用户','sf':'area_cy'},
'cy_dpu':{'cn':u'付费用户数','sf':'area_cy'},
'cy_dip':{'cn':u'付费总额','sf':'area_cy'},
'location_cn':{'cn':u'国家'},
'pr_dsu':{'cn':u'日新增用户','sf':'area_pr'},
'pr_dau':{'cn':u'日活跃用户','sf':'area_pr'},
'pr_dpu':{'cn':u'付费用户数','sf':'area_pr'},
'pr_dip':{'cn':u'付费总额','sf':'area_pr'},
'location_pr':{'cn':u'省份'},

# 应用列表
'apps_dau':{'cn':u'新增用户','sf':'app_sum'},
'apps_dsu':{'cn':u'活跃用户','sf':'app_sum'},
'apps_pun':{'cn':u'玩牌用户','sf':'app_sum'},
'apps_dpu':{'cn':u'付费用户','sf':'app_sum'},
'apps_dip':{'cn':u'用户收入','sf':'app_sum'},
'fgamefsk':{'cn':''},

'apps_c_dau':{'cn':u'新增用户','sf':'app_c_sum'},
'apps_c_dsu':{'cn':u'活跃用户','sf':'app_c_sum'},
'apps_c_pun':{'cn':u'玩牌用户','sf':'app_c_sum'},
'apps_c_dpu':{'cn':u'付费用户','sf':'app_c_sum'},
'apps_c_dip':{'cn':u'用户收入','sf':'app_c_sum'},

    # 系统设置-指标说明：表头
    "ename":    {"cn": u"指标名称（英文）"},
    "cname":    {"cn": u"指标名称（中文）"},
    "tips":     {"cn": u"定义"},
    "fexplain": {"cn": u"说明"},

}

dims_add_noly = {
    'sorder': 'fm_id',
    'fpay'  : 'fm_id',
    'fuser' : 'fm_id',
}

sp_hx_0 = ['sp_level','bd_level','ed_level','drupt_bal','sp_flevel',
           'sp_ybackplay','sp_1drpun','sp_pn','sp_actpn','entrance_pay']

first_col = {
    #'24h_aunum':'fname',
    #'24h_aucnt':'fname',

}

def get_sql_flag(dims_str):
    if dims_str == '':
        return []
    dimlist = dims_str.split('|')
    sql_flag = []
    for d in dimlist:
        sf = dim_labels.get(d,{}).get('sf','')
        if sf:
            sql_flag.append(sf)
    return list(set(sql_flag))

def add_only(dims):
    return dims_add_noly.get(dims,'fuck_all')

def dimChinese( dim ):
    if dim not in dim_labels:
        return dim
    return dim_labels[dim].get('cn',dim)

def dimInfo(dim,info):
    if dim not in dim_labels:
        return dim
    return dim_labels[dim].get(info,None)


# *_* coding:utf-8 *_*
from dc_redis_frame import cache_base
from flask import g


#@todo
#将所有的游戏，平台，大厅，子游戏，版本，终端，推广渠道的id和name缓存的redis里
def set_gpv_id_name_to_redis():
    keys = ["game","platform","hall","terminaltype","version"]
    for key in keys:
        datas = load_info_from_pg(keyname=key)
        set_name_id_to_redis(key, datas)
    set_name_id_to_redis("subgame",load_subgame_from_pg())
    chanels = load_channel_from_pg()
    set_channel_to_redis("channel", chanels)

def load_info_from_pg(keyname="game"):
    sql = "select distinct f%(keyname)sfsk,f%(keyname)sname from dcnew.bpid_map"
    datas = g.db.query(sql % { "keyname" : keyname})
    return datas

def load_subgame_from_pg():
    sql = "select fsubgamefsk,fsubgamename from dcnew.subgame_dim"
    datas = g.db.query(sql)
    return datas

def set_channel_to_redis(key,datas):
    redis_db = g.redis_db
    for row in datas:
        data = {}
        data[str(row["fchannel_id"])] = row["name"]
        redis_db.hmset(key,data)

def load_channel_from_pg():
    sql = "select fchannel_id,name from analysis.dc_channel"
    datas = g.db.query(sql)
    return datas

def set_name_id_to_redis(key,datas):
    redis_db = g.redis_db
    for row in datas:
        data = {}
        data[str(row["f" + key + "fsk"])] = row["f" + key + "name"]
        redis_db.hmset(key,data)

def get_name_by_id(key,id = 0):
    keydict = {"game" : "game","plat" : "platform","hall" : "hall","terminal":"terminaltype","ver":"version","subgame":"subgame","channel":"channel"}
    key = keydict[key]
    redis_db = g.redis_db
    if not redis_db.exists(key):
        set_gpv_id_name_to_redis()
    if redis_db.hget(key,str(id)) is None:
        set_gpv_id_name_to_redis()
    result = redis_db.hget(key,str(id))
    return result

def set_user_select_gpv_to_redis(fuid,select_gpv):
    redis_db = g.redis_db
    pass

# _*_ coding:utf-8 _*_
# 获取和更新token
import requests, json
from config.default import error_page, APPID, SECRET
from database.mysql import MysqlDB
import logging
token_table = 'tokens'



def token_passed(id='001'):
    pass

def update_token(id='001'):
    token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
    APPID, SECRET)
    try:
        token_res = requests.get(token_url)
        token = json.loads(token_res.text)['access_token']
        MysqlDB.insert("update %s set access_token='%s' WHERE id='%s'" % (token_table, token, id) )
    except Exception as e:
        logging.error("update access_token error: %s" % e)

def get_access_token(id='001'):
    try:
        data = MysqlDB.run_query("select * from %s WHERE id='%s'" %  (token_table, id) )
        return data[0]['access_token']
    except Exception as e:
        logging.error("get access_token error: %s" % e)
        return None

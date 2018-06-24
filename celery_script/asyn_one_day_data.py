# _*_ coding:utf-8 _*_

from config.default import projectID, salt, REMOTE_URL, TEACHER_TABLE
import json, requests
from database.mysql import MysqlDB

def aysn_one_day_data():
    data = {
        'projectID': projectID,
        'salt': salt,
    }

    res = requests.post(url=REMOTE_URL + '/getDataToday_v4/', data=data)

    weixin_data = json.loads(json.loads(res.text)['list'])
    print weixin_data
    # for user in weixin_data:
    #     fakeName = user['fakeName']
    #     nickName = user['nickName']
    #     for rundata in user['list']:
    #         scoreNow = rundata['scoreNow']
    #         dateString = rundata['dateString']
    #
    #         sql = "insert into %s (fakeName,nickName,scoreNow,dateString)" \
    #               " VALUES ('%s','%s',%s,%s)  ON duplicate KEY UPDATE scoreNow=%s" % (TEACHER_TABLE, fakeName, nickName, scoreNow, dateString, scoreNow)
    #
    #         print sql
    #         MysqlDB.insert(sql)
    #
aysn_one_day_data()
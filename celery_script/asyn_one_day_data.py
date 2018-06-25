# _*_ coding:utf-8 _*_

from config.default import projectID, salt, REMOTE_URL, TEACHER_TABLE
import json, requests
from database.mysql import MysqlDB
import time
from common.function import get_day
def aysn_one_day_data():
    data = {
        'projectID': projectID,
        'salt': salt,
    }

    res = requests.post(url=REMOTE_URL + '/getDataToday_v4/', data=data)

    weixin_data = json.loads(json.loads(res.text)['list'])
    print weixin_data
    for user in weixin_data:
        fakeName = user['fakeName']
        nickName = user['nickName']
        timestamp = time.time()
        scoreNow = user['scoreNow']
        dateString = str(get_day())
        sql = "insert into %s (fakeName,nickName,scoreNow,dateString)" \
              " VALUES ('%s','%s',%s,%s)  ON duplicate KEY UPDATE scoreNow=%s, update_time=%s" % (TEACHER_TABLE,
                                                                                                  fakeName, nickName,
                                                                                                  scoreNow, dateString,
                                                                                                  scoreNow, timestamp)

        print sql
        MysqlDB.insert(sql)

aysn_one_day_data()
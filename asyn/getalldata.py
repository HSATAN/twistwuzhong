# _*_ coding:utf-8 _*_

import requests
from config.default import projectID, salt, REMOTE_URL, TEACHER_TABLE
import json
from database.mysql import MysqlDB
data = {
    'projectID': projectID,
    'salt': salt,
}

res = requests.post(url= REMOTE_URL + '/getDataAll_v4/', data=data)

weixin_data = json.loads(json.loads(res.text)['list'])

for user in weixin_data:
    fakeName = user['fakeName']
    nickName = user['nickName']
    for rundata in user['list']:
        scoreNow = rundata['scoreNow']
        dateString = rundata['dateString']

        sql = "insert into %s (fakeName,nickName,scoreNow,dateString)" \
              " VALUES ('%s','%s',%s,%s)" % (TEACHER_TABLE, fakeName, nickName, scoreNow, dateString)

        print sql
        MysqlDB.insert(sql)
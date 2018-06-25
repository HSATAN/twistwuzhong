# _*_ coding:utf-8 _*_

import requests, json
from config.default import error_page, APPID, SECRET
from weixin.token_action import get_access_token

data = {
    "kf_account": "maobazhongxue001",
    "nickname": "茅坝中学001",
    "password": "maobazhongxue001"
}
token = get_access_token()
url = 'https://api.weixin.qq.com/customservice/kfaccount/add?access_token=%s' % token
r = requests.post(url=url,data=data)

print r.text
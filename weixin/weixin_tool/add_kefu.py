# _*_ coding:utf-8 _*_

import requests
from default import error_page, APPID, SECRET
url = 'https://api.weixin.qq.com/customservice/kfaccount/add?access_token=renhuaishimaobazhongxue'

data = {
    "kf_account": "maobazhongxue001",
    "nickname": "茅坝中学001",
    "password": "maobazhongxue001"
}
token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (APPID, SECRET)

token_res = requests.get(token_url)
print token_res.text
r = requests.post(url=url,data=data)

print r.text
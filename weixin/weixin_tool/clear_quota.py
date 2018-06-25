# _*_ coding:utf-8 _*_
from weixin.token_action import get_access_token
import requests
import json
from config.default import APPID
url = "https://api.weixin.qq.com/cgi-bin/clear_quota?access_token=%s" % get_access_token()
res = requests.post(url=url, data=json.dumps({"appid": APPID}))
print res.text
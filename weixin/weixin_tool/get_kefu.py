# _*_ coding:utf-8 _*_
import requests
from weixin.token_action import get_access_token

url = 'https://api.weixin.qq.com/cgi-bin/customservice/getkflist?access_token=%s' % get_access_token()

res = requests.get(url)

print res.text
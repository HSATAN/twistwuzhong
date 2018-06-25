# _*_ coding:utf-8 _*_
import requests
import json
from weixin.token_action import get_access_token
url = 'https://api.weixin.qq.com/cgi-bin/message/mass/send?access_token=%s'

data = {
   "touser":[
    "o-u061Sh5MRebTgbZWeRLJaxYqD4","o-u061ZFbWfu2tG_F6hr708cpXLY",
       "o-u061XHdHtcqSzk3R6mfIldMSq4"
   ],
    "msgtype": "text",
    "text": { "content": "19631111555111444425"}
}
def send_message_all(data):
    """
    群发消息
    :param data: 消息体
    :return:
    """
    token = get_access_token()
    res = requests.post(url=url % token, data=json.dumps(data, ensure_ascii=False))

    print res.text

send_message_all(data)
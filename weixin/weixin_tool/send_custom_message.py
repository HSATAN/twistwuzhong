# _*_ coding:utf-8 _*_
import requests
import json
from weixin.token_action import get_access_token
url = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token=%s'

# data = {
#    "touser":[
#     "o-u061Sh5MRebTgbZWeRLJaxYqD4","o-u061ZFbWfu2tG_F6hr708cpXLY",
#    ],
#     "msgtype": "text",
#     "text": { "content": "196311115fgdasdfgfdsfsdfsdfdshjklgdfgd55111444425"}
# }

params = {
   "filter":{
      "is_to_all":False,
      "tag_id":100
   },
   "text":{
      "content":"CONTENT"
   },
    "msgtype":"text"
}
def send_message_all(data):
    """
    群发消息
    :param data: 消息体
    :return:
    """
    token = get_access_token()
    res = requests.post(url=url % token, data=json.dumps(params, ensure_ascii=False))

    print res.text

send_message_all(params)
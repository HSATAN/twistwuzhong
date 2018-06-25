# _*_ coding:utf-8 _*_
from weixin.token_action import get_access_token
import requests
def upload_img():
    token = get_access_token()
    data = {"access_token": token,
            "media": ""}
    url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=%s" % token
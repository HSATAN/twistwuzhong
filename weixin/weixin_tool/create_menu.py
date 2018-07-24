# _*_ coding:utf-8 _*_
"""
微信公众号创建自定义菜单

"""
from weixin.weixin_config import create_menu_url
import requests
import json
from config.default import APPID
from weixin.token_action import get_access_token
token = get_access_token()
redirect_url = "http%3a%2f%2fwww.myenger.com%2fopenid"
base_url = "https://open.weixin.qq.com/connect/oauth2" \
      "/authorize?appid=%s&redirect_uri=%s&" \
      "response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect" % (APPID, redirect_url)
data = {"button":
        [
            {
                "name": "微信运动",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "查看今日排名",
                        "url": "http://www.myenger.com/todayrank"
                    },
                    {
                        "type": "view",
                        "name": "查看我的数据",
                        "url": "http://www.myenger.com/persondata"
                    },
{
                        "type": "view",
                        "name": "获取openid",
                        "url": base_url
                    }
                ]
            },
            {
                "name": "茅坝中学",
                "type": "click",
                "key": "MB_MAIN_PAGE"
            },
            {
                "name": "其它",
                "type": "click",
                "key": "MB_QITA_PAGE"
            }
        ]
}

res = requests.post(url=create_menu_url % token, data=json.dumps(data, ensure_ascii=False))
print res.text
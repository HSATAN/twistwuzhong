# _*_ coding:utf-8 _*_
"""
微信公众号创建自定义菜单

"""
from weixin.weixin_config import create_menu_url
import requests
import json
from weixin.token_action import get_access_token
token = get_access_token()

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
                        "url": "http://www.myenger.com/openid"
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
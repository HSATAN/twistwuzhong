# _*_ coding:utf-8 _*_
"""
微信公众号创建自定义菜单

"""
from weixin.weixin_config import create_menu_url
import requests
import json
token = "10_w0MOaSFm5GbET3uVPvR4ghG4AFvQ-mlW5wB739YJ9O-Rh0OMQMhXtLR1ET_JWUoW3Pnf0Ce6yNEj5cwqvP_1F5e9mkTMUbtlNbQyGqTRDC9yBdjzshJMAipseOZ-O4tpxtOzsRzi-qu56gBwPHQdAAALDM"

data = {"button":
        [
            {
                "name": "微信运动",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "今日排名",
                        "url": "http://www.myenger.com/allrank"
                    },
                    {
                        "type": "view",
                        "name": "查看我的数据",
                        "url": "http://www.myenger.com/personrank"
                    }
                ]
            },
            {
                "name": "茅坝中学",
                "type": "click",
                "key": "MB_MAIN_PAGE"
            }
        ]
}

res = requests.post(url=create_menu_url % token, data=json.dumps(data, ensure_ascii=False))
print res.text
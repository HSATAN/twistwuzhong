# _*_ coding:utf-8 _*_
"""
微信公众号创建自定义菜单

"""
from weixin.weixin_config import create_menu_url
import requests
import json
token = "10_9kRISUY40XkAjr-e-TzbiNopt--IELkMyZPccZg9CXc49vZnlsJc2RQQoO6huDyQjYraSRCl7L6xnJskrPMsugDWEUOzhyDq_NqJkmMeYcfTp1QnuGUkpjW-d7WAw-0IaH_BHZJT-iqh5FzqVLWeACAOEP"

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
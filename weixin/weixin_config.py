# _*_ coding:utf-8 _*_

create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s'

access_token = ""

scope_url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
            "appid=%s&secret=%s&code=%s&grant_type=authorization_code"
"""
网页授权url
"""
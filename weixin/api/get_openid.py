# _*_ coding:utf-8 _*_
from twisted.web.resource import Resource
import logging
from weixin.weixin_config import scope_url
from config.default import APPID, SECRET
import requests
import json
from weixin.function import get_openid
class OpenId(Resource):

    def render_GET(self, request):

        flag, openid = get_openid(request)
        if flag:
            return openid
        else:return "获取open id失败"
# _*_ coding:utf-8 _*_
from twisted.web.resource import Resource

class OpenId(Resource):

    def render_GET(self, request):
        return "get openid"

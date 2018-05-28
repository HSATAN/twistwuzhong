# _*_ coding:utf-8 _*_
from __future__ import print_function
from twisted.web.resource import Resource
import json


class BaseResource(Resource):

    def render_HEAD(self, request):
        return self.real_HEAD(request)
        pass

    def render_GET(self, request):
        return self.real_GET(request)
        pass

    def render_POST(self, request):
        return ujson.dumps(self.real_POST(request))

    def real_HEAD(self, request):
        pass

    def real_GET(self, request):
        pass

    def real_POST(self, request):
        pass






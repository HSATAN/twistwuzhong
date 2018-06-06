# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import json
import logging

class GetCode(Resource):
    def render_GET(self, request):
        return 'NDeHTSMiVI1x3rfh'
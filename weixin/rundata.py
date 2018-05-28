# _*_ coding:utf-8 _*_
from __future__ import print_function
from baseresource.greenresource import BaseResource
from lxml import etree
import random
import logging

class RunData(BaseResource):

    back_data = ["我是智能", "你好", "你是"]
    data_length = 0
    def __init__(self):
        BaseResource.__init__(self)
    def real_POST(self, request):
        message = "这是测试微信网页"
        return message
    def real_GET(self, request):
        try:
            echostr = request.args.get('echostr')[0]
            return echostr
        except Exception as e:
            logging.info("访问错误")
            print("微信验证失败")
        return "非法访问"

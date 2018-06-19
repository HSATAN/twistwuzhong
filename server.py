# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import json
import logging
import requests
import re
from common.function import get_day
from weixin.api.person_rank import PersonRank
from weixin.api.all_rank import AllRank
from data.text import text1, text2, fakeName
from config.default import error_page, APPID, SECRET
from data.default_html import default_html
from weixin.rundata import RunData
from weixin.api.get_code import GetCode
from weixin.weixin_function import parse_text, parse_url
from weixin.query_data import get_today_data

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("", Index())
        self.putChild("rundata",RunData())
        self.putChild("wx", WXCheck())
        self.putChild("MP_verify_NDeHTSMiVI1x3rfh.txt", Auth())
        self.putChild("personrank", PersonRank())
        self.putChild("allrank", AllRank())
        self.putChild("test", Test())
        self.putChild("querydata", QueryData())
        self.putChild("today", Today())

class Today(Resource):
    """
    返回当日数据
    """
    def render_POST(self, request):
        data = get_today_data()
        print data
        return json.dumps(data)

class QueryData(Resource):
    def render_POST(self, request):
        start_date = request.args.get("startdate")[0]
        end_date = request.args.get("enddate")[0]
        return json.dumps({"data": "黄开杰"})
class Test(Resource):
    """
    测试网页
    """
    def render_GET(self, request):
        from weixin.html.all_rank_html import  all_rank_html_text
        return all_rank_html_text

class Auth(Resource):
    def render_GET(self, request):
        return 'NDeHTSMiVI1x3rfh'

class WXCheck(Resource):
    """
    微信服务器验证
    """
    def render_GET(self,request):
        try:
            # callback_token = request.args.get('callback_token')[0]
            echostr = request.args.get('echostr')[0]
            return echostr
        except Exception as e:
            logging.info("访问错误")
            print("微信验证失败")
        return "非法访问"

    def render_POST(self, request):
        """
        接收处理公众号用户消息
        :param request:
        :return:
        """
        try:
            # receiveData = parse_text(request)
            receiveData = parse_url(request)
            print(receiveData)
            logging.info(receiveData)
            return receiveData
        except Exception as e:
            logging.info("解析消息错误 %s" % e)


class Index(Resource):

    def render_GET(self,request):
        try:
            id = request.args.get('id')[0]
            print id
            fn = fakeName % id
            logging.info(fn)
            return text1 + fn+text2
        except Exception as e:
            try:
                code = request.args.get('code')[0]
                url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % (APPID,SECRET,code)
                res = requests.get(url)
                logging.info(res.text)
                logging.info("code =  %s" % code)
            except:
                pass
            return default_html


if __name__ == '__main__':
    logfile = 'log'
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/xiaochengxu/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(9999, Site(Root()))
    reactor.run()
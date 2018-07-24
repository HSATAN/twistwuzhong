# _*_ coding:utf-8 _*_
from twisted.web.resource import Resource
import logging
from weixin.weixin_config import scope_url
from config.default import APPID, SECRET
import requests
import json
class OpenId(Resource):

    def render_GET(self, request):
        try:
            code = request.args.get("code")[0]
            print code
            logging.info("网页授权成功: code=%s" % code)
            url = scope_url % (APPID, SECRET, code)
            print url
            try:
                res = requests.get(url=url)
                content = json.loads(str(res.text))
                print content
                logging.info("content=%s" % content)
                logging.info("openid=" % content["openid"])
                return "你的openid为 %s" % content["openid"]
            except Exception as e:
                logging.info("获取openid失败：%s" % e)
                return "获取openid失败 %s" % e
        except Exception as e:
            logging.info("网页授权失败，获取code错误 ： %s" % e)
            return "网页授权失败"

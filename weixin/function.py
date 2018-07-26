# _*_ coding:utf-8 _*_
import logging
import json
import requests
from config.default import APPID, SECRET
from weixin_config import scope_url

def get_openid(request):
    try:
        code = request.args.get("code")[0]
        print code
        logging.info("网页授权成功: code=%s" % code)
        url = scope_url % (APPID, SECRET, code)
        print url
        try:
            res = requests.get(url=url)
            content = json.loads(res.text.encode("raw_unicode_escape").decode('utf8'))
            logging.info("content=%s" % content)
            # logging.info("openid=" % content["openid"])
            openid = str(content["openid"])
            return True, openid
        except Exception as e:
            logging.info("获取openid失败：%s" % e)
            return False, "获取openid失败 %s" % e
    except Exception as e:
        logging.info("网页授权失败，获取code错误 ： %s" % e)
        return False, "网页授权失败"
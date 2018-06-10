# _*_ coding:utf-8 _*_
from lxml import etree
import random
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def parse_text(request):

    """
    处理微信text消息
    :param request:
    :return:
    """
    receiveData = request.content.read()  # 获取微信发送过来的body
    logging.info(receiveData)
    data = etree.fromstring(receiveData)
    ToUserName = data.find('ToUserName').text
    FromUserName = data.find('FromUserName').text
    CreateTime = data.find('CreateTime').text
    Content = data.find('Content').text
    print(Content)
    Content = "您好，你的消息我们已收到，将尽快为您处理，感谢您的关注！"
    # print(receiveData)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>' % (
    FromUserName, ToUserName, CreateTime, Content)
    return message
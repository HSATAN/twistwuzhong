# _*_ coding:utf-8 _*_
from lxml import etree
import random
import logging
import sys
from default import HOST_URL
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
    Content = "查看运动数据请点击下面的地址\n" + HOST_URL
    # print(receiveData)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>' % (
    FromUserName, ToUserName, CreateTime, Content)
    return message

def parse_url(request):

    """
    返回消息连接
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
    Content = "查看运动数据请点击下面的地址\n" + HOST_URL
    # print(receiveData)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>' % (
        FromUserName, ToUserName, CreateTime, Content)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName>' \
              '<![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType>' \
              '<![CDATA[link]]></MsgType><Title><![CDATA[公众平台官网链接]]>' \
              '</Title><Description><![CDATA[公众平台官网链接]]></Description><Url><![CDATA[%s]]></Url>' \
              '<MsgId>%s</MsgId></xml>' % (FromUserName, ToUserName, CreateTime, Content, HOST_URL)
    return message
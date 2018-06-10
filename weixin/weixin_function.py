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
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName>' \
              '<CreateTime>%s</CreateTime>' \
              '<MsgType><![CDATA[text]]></MsgType>' \
              '<Content><![CDATA[%s]]></Content></xml>' % (
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
    MessageId = data.find('MsgId').text
    print(Content)
    Content = "您好，你的消息我们已收到，将尽快为您处理，感谢您的关注！"
    Content = "查看运动数据请点击下面的地址\n" + HOST_URL
    # print(receiveData)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName>' \
              '<![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>' % (
        FromUserName, ToUserName, CreateTime, Content)
    message = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName>' \
              '<![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType>' \
              '<![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount>' \
              '<Articles>' \
              '<item>' \
              '<Title>< ![CDATA[微信运动数据统计] ]></Title> ' \
              '<Description>< ![CDATA[%s] ]></Description>' \
              '<PicUrl><![CDATA[http://bpic.588ku.com/element_origin_min_pic/17/05/02/1361c3cbd95871860621fff45f5b86ba.jpg!r650]]></PicUrl>' \
              '<Url>< ![CDATA[%s] ]></Url>' \
              '</item>' \
              '</Articles></xml>' % (FromUserName, ToUserName, CreateTime, Content, HOST_URL)
    return message
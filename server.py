# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import json
import logging
import re
from weixin.rundata import RunData
class Root(Resource):

    def __init__(self):
        Resource.__init__(self)

        self.putChild("", RunData())




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
# _*_ coding:utf-8 _*_

"""
个人数据统计
"""

from twisted.web.resource import Resource


class PersonRank(Resource):

    def render_GET(self, request):
        return "这是个人数据排名"
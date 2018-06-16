# _*_ coding:utf-8 _*_


"""
所有排名数据统计
"""

from twisted.web.resource import Resource


class AllRank(Resource):

    def render_GET(self, request):
        return "所有数据排名"
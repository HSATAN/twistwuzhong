# _*_ coding:utf-8 _*_

"""
个人数据统计
"""

from twisted.web.resource import Resource
from weixin.html.all_rank_html import all_rank_html_text

class PersonRank(Resource):

    def render_GET(self, request):
        return all_rank_html_text
# _*_ coding:utf-8 _*_

from database.mysql import MysqlDB
from common.function import get_day
from config.default import TEACHER_TABLE
def get_today_data():
    """
    查询今日数据
    :return:
    """
    print "select * from %s WHERE dateString='%s'" % (TEACHER_TABLE, get_day())
    today_data = MysqlDB.run_query("select * from %s WHERE dateString='%s' ORDER BY scoreNow asc" % (TEACHER_TABLE, get_day()))
    return today_data

def query_data_by_date(start_time=None, end_time=None):
    today_data = MysqlDB.run_query("select * from %s WHERE dateString='%s' ORDER BY scoreNow asc" % (TEACHER_TABLE, get_day()))
    return today_data

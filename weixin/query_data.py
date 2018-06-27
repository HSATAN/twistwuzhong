# _*_ coding:utf-8 _*_

from database.mysql import MysqlDB
from common.function import get_day
from config.default import TEACHER_TABLE

def count_time(key=None):
    today = str(get_day())
    if not key:
        return today, today
    elif key=="current_week":
        pass


def get_today_data():
    """
    查询今日数据
    :return:
    """
    print "select * from %s WHERE dateString='%s'" % (TEACHER_TABLE, get_day())
    today_data = MysqlDB.run_query("select * from %s WHERE dateString='%s' ORDER BY scoreNow asc" % (TEACHER_TABLE, get_day()))
    return today_data

def query_data_by_date(key=None):

    if not key:
        return MysqlDB.run_query("select * from %s WHERE dateString='%s' ORDER BY scoreNow asc" % (TEACHER_TABLE, get_day()))
    else:
        startTime, endTime = count_time(key)
        sql = "SELECT fakeName,nickName,dateString,openID, SUM(scoreNow) AS scoreNow" \
              " from teacher WHERE dateString>='%s' AND dateString <= '%s'  GROUP BY fakeName " % (startTime, endTime)
        return {}
print query_data_by_date()
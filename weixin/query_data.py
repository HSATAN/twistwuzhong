# _*_ coding:utf-8 _*_

from database.mysql import MysqlDB
from common.function import get_day
from config.default import TEACHER_TABLE
from datetime import datetime, timedelta
import time


def count_time(key=None):
    today = str(get_day())
    if not key  or key == "today":
        return today, today
    elif key == "current_week":
        return str(get_day(time.mktime((datetime.now() + timedelta(days=-datetime.today().weekday())).timetuple()))), str(get_day())
    elif key == 'last_week':
        return str(get_day(time.mktime((datetime.now() + timedelta(days=-datetime.today().weekday()-7)).timetuple()))), str(get_day(time.mktime((datetime.now() + timedelta(days=-datetime.today().weekday()-1)).timetuple())))
    elif key == "month":
        return str(get_day(time.mktime((datetime.now() + timedelta(days=-datetime.today().day+1)).timetuple()))), str(get_day())
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
              " from teacher WHERE dateString>='%s' AND dateString <= '%s'  GROUP BY fakeName ORDER BY scoreNow ASC " % (startTime, endTime)
        print sql
        data = MysqlDB.run_query(sql)
        print data
        return  data


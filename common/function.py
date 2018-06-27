# _*_ coding:utf-8 _*_
import time
def timestamp_to_date(timestamp):
    localtime = time.localtime(timestamp)
    date = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    return date

def get_day(timestamp=None):
    if not timestamp:
        timestamp = time.time()
    localtime = time.localtime(timestamp)
    date = int(time.strftime("%Y%m%d", localtime))
    return date
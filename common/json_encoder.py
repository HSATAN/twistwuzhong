# _*_ coding:utf-8 _*_
import json
from datetime import datetime

class DatetimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, o)

# _*_ coding:utf-8 _*_

from kombu import Exchange, Queue

from celery.schedules import  crontab
from config.default import REDIS_PASSWORD, REDIS_DB, REDIS_PORT, REDIS_HOST
from config.default import MYSQL_HOST, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_USER
BROKER_URL = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DB)
print BROKER_URL

CELERY_RESULT_BACKEND = 'db+mysql://%s:%s@%s/celery' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST)

print CELERY_RESULT_BACKEND

CELERY_RESULT_DB_TABLENAMES = {
    'task': 'taskmeta',
    'group': 'groupmeta',
}


# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_ENABLE_UTC = True

from  datetime import timedelta

# 定时任务

CELERYBEAT_SCHEDULE = {
    "asyn_one_day":
        {
            "task": "celery_script.celery_tasks.aysn_one_day_data",
            "schedule": crontab(minute='*/3'),
            "args": None,
        },
}

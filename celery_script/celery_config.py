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
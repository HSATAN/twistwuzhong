# _*_ coding:utf-8 _*_

import subprocess
from database.mysql import MysqlDB
from celery import Celery

celery_instance = Celery()
celery_instance.config_from_object('celery_script.celery_config')

@celery_instance.task()
def add(x, y):
    return x + y
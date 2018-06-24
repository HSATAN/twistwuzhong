# _*_ coding:utf-8 _*_

import redis
from config.default import REDIS_DB, REDIS_PASSWORD, REDIS_HOST, REDIS_PORT

class MyRedis(object):

    """
    redis连接处理
    """
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)
    r = redis.Redis(connection_pool=pool)

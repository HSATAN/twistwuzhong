# _*_ coding:utf-8 _*_

import logging
import pymysql
from config import default as config

class MysqlDB(object):

    conn = pymysql.connect(host=config.MYSQL_HOST,
                           port=config.MYSQL_PORT,
                           password=config.MYSQL_PASSWORD,
                           db=config.MYSQL_DATABASE,
                           user=config.MYSQL_USER,
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()

    @classmethod
    def insert(cls, operation):
        try:
            cls.cursor.execute(operation)
            cls.commit()
        except Exception as e:
            logging.error("insert error: %s" % e)
            cls.reconn()
            # cls.rollback()
            # cls.commit()
    @classmethod
    def reconn(cls):
        try:
            cls.cursor = cls.conn.cursor()
        except Exception as e:
            logging.error("reconn error %s" %e)

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def commit(cls):
        cls.conn.commit()

    @classmethod
    def rollback(cls):
        cls.conn.rollback()

    @classmethod
    def run_query(cls, operate):
        try:
            cls.cursor.execute(operate)
            return cls.cursor.fetchall()
        except Exception as e:
            logging.error(e)
            try:
                cls.error()
            except:
                pass

    @classmethod
    def query_all(cls, operate):
        cls.cursor.execute(operate)
        return cls.cursor.fetchall()
    @classmethod
    def error(cls):
        cls.rollback()
        cls.commit()

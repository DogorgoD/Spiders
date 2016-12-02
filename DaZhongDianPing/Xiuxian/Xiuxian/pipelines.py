# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from scrapy.conf import settings


class MySQLPipeline(object):
    def __init__(self):
        # MYSQL_HOST = 'localhost'
        # MYSQL_DBNAME = 'DianPing'
        # MYSQL_USER = 'debian-sys-maint'
        # MYSQL_PASSWD = 'V9kflS1yEB4h3bRw'
        self.connection = MySQLdb.connect(
            host = settings['MYSQL_HOST'],
            port = 3306,
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            db = settings['MYSQL_DBNAME'],
        )


    def process_item(self, item, spider):
        cur = self.connection.cursor()
        insert_url = 'insert into url values(%s, %s)'
        cur.execute(insert_url, (item['url'], item['id']))
        cur.close()
        self.connection.commit()
        return item


# class XiuxianPipeline(object):
#     def process_item(self, item, spider):
#         return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import pymysql
from scrapy.exceptions import NotConfigured



class MaoyanzuoyePipeline:
    # def process_item(self, item, spider):
    #     return item
    # def process_item(self, item, spider):
    #     print(f'process_item: {item}')
    #     write_clo=[item['name'],item['ftype'],item['sdate']]
    #     #process_item: {'ftype': ' 剧情 , 爱情 ', 'name': '荞麦疯长', 'sdate': '2020-08-25中国大陆上映'}
    #     dataframe = pd.DataFrame(columns=(write_clo))
    #     dataframe.to_csv("test.csv",mode='a', index=False, sep=',')
    #     return item
    def __init__(self,mysql_config):
        self.host=mysql_config['host']
        self.port=mysql_config['port']
        self.user=mysql_config['user']
        self.passwd=mysql_config['passwd']
        self.db=mysql_config['db']

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('HTTP_PROXY_LIST'):
            raise NotConfigured
        return cls(mysql_config=crawler.settings.get('MYSQL_CONFIG'))

    def open_spider(self, spider):       
        self.connection = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.passwd,
                             db=self.db,
                             charset='utf8',)

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self,item, spider):
        sql = "INSERT INTO MAOYANF(NAME, FTYPE, SDATE) \
                VALUES ('%s', '%s', '%s')" % \
                (item["name"],item["ftype"],item["sdate"])
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f'ERROR: {e}')
            self.connection.rollback()
        

        
        
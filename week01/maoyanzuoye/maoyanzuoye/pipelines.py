# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MaoyanzuoyePipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        print(f'process_item: {item}')
        write_clo=[item['name'],item['ftype'],item['sdate']]
        #process_item: {'ftype': ' 剧情 , 爱情 ', 'name': '荞麦疯长', 'sdate': '2020-08-25中国大陆上映'}
        dataframe = pd.DataFrame(columns=(write_clo))
        dataframe.to_csv("test.csv",mode='a', index=False, sep=',')
        return item
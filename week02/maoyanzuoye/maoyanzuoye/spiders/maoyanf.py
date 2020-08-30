#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import requests
import lxml.etree
from maoyanzuoye.items import MaoyanzuoyeItem

class MaoyanfSpider(scrapy.Spider):
    name = 'maoyanf'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3/']

    #def parse1(self, response):
        #print(dir(response))
    #    return response


    def start_requests(self):
        url_login='https://passport.meituan.com/account/unitivelogin?service=maoyan&continue=https%3A%2F%2Fmaoyan.com%2Fpassport%2Flogin%3Fredirect%3D%252F'
        url1='https://maoyan.com/films?showType=3/'
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        # 声明为字典使用字典的语法赋值
        header = {}
        header['user-agent'] = user_agent
        response=requests.get(url1, headers=header)
        #yield scrapy.Request(url=url1,callback=self.parse1)
        #print(f'--{response.text}--')
        f = Selector(response=response)
        #print(f)
        urls=f.xpath(f'//a[re:test(@href, "/films/\d+$")]/@href').getall()
        item=MaoyanzuoyeItem()
        for i in urls[0:10]:
            url='https://maoyan.com'+i
            #print(url)
            yield scrapy.Request(url=url,meta={'item':item},callback=self.parse2)

    def parse2(self, response):
        #print(response.url)
        item=response.meta['item']
        x=Selector(response=response)
        #print(x)
        name =  ','.join(x.xpath('//h1[@class="name"]/text()').extract())
        ftype = ','.join(x.xpath('//a[@class="text-link"]/text()').extract())
        sdate = ','.join(x.xpath('//li[re:test(., "^\d{4}-\d{2}-\d{2}.*$")]/text()').extract())
        print(f'parse2: {name},{ftype},{sdate}')
        item['name']=name
        item['ftype']=ftype
        item['sdate']=sdate
        yield item
# -*- coding: utf-8 -*-
import scrapy


class RandproxySpider(scrapy.Spider):
    name = 'randproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']
    # 通过header 查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)
        
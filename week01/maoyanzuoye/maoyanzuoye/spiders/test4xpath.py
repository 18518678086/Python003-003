#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import requests
import lxml.etree
import os
from scrapy import Selector

print(os.getcwd())
os.chdir('./github/Python003-003/week01/maoyanzuoye/maoyanzuoye/spiders/')
body = open('babai.html').read()
#使用scrapy自身的Selector解析文本
x = Selector(text=body)
name =  x.xpath('//h1[@class="name"]/text()')
ftype = x.xpath('//a[@class="text-link"]/text()')
date = x.xpath('//li[re:test(., "\d{4}-\d{2}-\d{2}.*")]/text()')
print(name.extract(),ftype.extract(),date.extract())

#!/usr/local/bin/python3
#coding: utf-8

import requests
import lxml.etree

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':user_agent}
myurl='https://movie.douban.com/subject/26754233/'

response = requests.get(myurl,headers=header)
selector = lxml.etree.HTML(response.text)


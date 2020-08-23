#!/usr/local/bin/python3
#coding: utf-8

import requests
from bs4 import BeautifulSoup as bs
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl='https://movie.douban.com/subject/26754233/'
response = requests.get(myurl,headers=header)



bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        # 获取所有链接
        print(atag.find('span').text)
        # 获取电影名字

for i in bs_info.find_all('div', attrs={'class': 'comment'}):
    for a in i.find_all('a'):
        print(atag.find('span').text)

#!/usr/local/bin/python3
#coding: utf-8

import requests
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
header = {'user-agent':user_agent}

myurl='https://movie.douban.com/subject/26754233/'
response = requests.get(myurl,headers=header)
print(response.text)
print(f'返回码是: {response.status_code}')


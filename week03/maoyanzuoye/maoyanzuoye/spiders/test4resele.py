#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests

url='https://shimo.im/lizard-api/auth/password/login'
data={'mobile': '+8618518678086','password': 'sm123456'}
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        # 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
header['referer']='https://shimo.im/login?from=home'
header['x-requested-with']= 'XmlHttpRequest'
header['x-source']= 'lizard-desktop'

with requests.Session() as s:
    r=s.post(url,headers=header,data=data)
    print(s.cookies.get_dict(),r.text,r.status_code)
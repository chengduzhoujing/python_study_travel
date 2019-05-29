# !/usr/bin/python3
# Author : Zhoujing
# Date : 2019/5/28 16:36
# Email : 854021135@qq.com

import requests
import telnetlib
import random
from bs4 import BeautifulSoup
import cchardet
from bs4.element import Tag
import re
# ua_list = [
#     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.0',
#     'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
#     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
#     'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.0.1 Safari/537.36'
#     ]
#
# for i in range(1,3):
#     r = requests.get(url='https://www.xicidaili.com/nn/{}'.format(i), headers={'User-agent': random.choice(ua_list)})
#     with r:
#         content = r.content
#         html = content.decode(encoding=cchardet.detect(content)['encoding'])
#         s = BeautifulSoup(html, 'lxml')
#         ts = s.find_all('tr',class_=True)
#         for t in ts:
#             ip, port,_,_,pro,*_ = list(t.stripped_strings)
#             try:
#                 telnetlib.Telnet(host=ip, port=int(port), timeout=3)
#             except Exception as e:
#                 pass
#             else:
#                 print('{}://{}:{}'.format(pro, ip, port))
url = 'https://api.bilibili.com/x/v2/reply?callback=jQuery172009453168168781034_1559041261972&jsonp=jsonp&pn=1&type=1&oid=53860095&sort=2&_=1559041262903'
headers = {
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Connection': "keep-alive",
    'Host': "api.bilibili.com",
    'Referer': "https://www.bilibili.com/v/documentary/travel/",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    'Cache-Control': "no-cache",
    'Postman-Token': "7cfb47b9-6f2c-44f3-a51f-82bac5bb0fc6"
    }
r = requests.get(url=url, headers=headers)
print(r.text.split('(',1)[-1].rsplit(')',1)[0])


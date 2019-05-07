#coding=utf-8
import requests
import json

# url1 = "http://www.cnblogs.com/yoyoketang/"
#
# r = requests.get(url1)
# print(r.status_code)
# print(r.text)

# url2 = "http://zzk.cnblogs.com/s/blogpost"
# my_params = {"Keywords": "yoyoketang"}
# r2 = requests.get(url2, params=my_params)
# print(r2.status_code)
# print(r2.text)

# url3 = "https://api.github.com/events"
# r3 = requests.get(url3)
# print(r3.json())

url4 = "https://www.baidu.com"
r4 = requests.get(url4)
print(r4.content.decode())
print(r4.cookies)

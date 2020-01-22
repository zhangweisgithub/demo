# -*- coding: utf-8 -*-
import requests

url = "http://www.baidu.com"
response = requests.get(url)
print(type(response.cookies))

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)

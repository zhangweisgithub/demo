# !/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import parse

"""
url：待解析的url
scheme=''：假如解析的url.q没有协议,可以设置默认的协议,如果url有协议，设置此参数无效
allow_fragments=True：是否忽略锚点,默认为True表示不忽略,为False表示忽略
"""
url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
# url = 'https:10.9.244.33:9001/info/1004608738?wd=123&page=20#Catalog'

result = parse.urlparse(url=url, scheme='http', allow_fragments=True)

print(result)
print(result.scheme)
"""
scheme:	计划; 方案; 体系; 体制; 阴谋; 诡计; 计谋;
(scheme='https', netloc='bookidian.com', path='/info/1004608738', params='', query='wd=123&page=20', fragment='Catalog')
scheme:表示协议
netloc:域名
path:路径
params:参数
query:查询条件，一般都是get请求的url
fragment:锚点，用于直接定位页面的下拉位置，跳转到网页的指定位置
"""

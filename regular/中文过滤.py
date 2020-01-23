# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re

a = "not 404 found 张三 99 深圳"
# spilt()将str转换为列表, join()将list转换为str
list = a.split(" ")
print(list)  # ['not', '404', 'found', '\xe5\xbc\xa0\xe4\xb8\x89', '99', '\xe6\xb7\xb1\xe5\x9c\xb3']
res = re.findall("\d+|[a-zA-Z]+", a)
print(res)  # 匹配数字   匹配单词 ['not', '404', 'found', '99']
for i in res:
    list.remove(i)
new_str = " ".join(list)
print(new_str)

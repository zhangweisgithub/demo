# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = {'2710': None, 'heads': 0, 'tails': 0}
print(a.keys())  # .keys()返回的是一个对象，后面如果要加索引的话需要把对象转化为列表
if "2710" in a.keys():
    print("sf")
print(list(a.keys())[0])

for item in a.keys():
    print(item)

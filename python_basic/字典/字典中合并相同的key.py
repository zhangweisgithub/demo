# !/usr/bin/env python
# -*- coding: utf-8 -*-
list1 = [{"a": 123}, {"a": 23}, {"b": 12}]

"""方法一"""
dic = {}
for i in list1:
    for k, v in i.items():
        dic.setdefault(k, []).append(v)
print(dic)

"""方法二"""
print([{k: v} for k, v in dic.items()])

"""===================="""

a = {'2710': None, 'heads': 0, 'tails': 0}
print(a.keys())  # .keys()返回的是一个对象，后面如果要加索引的话需要把对象转化为列表

if "2710" in a.keys():  # 这里是可以执行的没有问题
    print("sf")
print(list(a.keys())[0])

print("----------------我是分割线----------------------")
for item in a.keys():
    print(item)

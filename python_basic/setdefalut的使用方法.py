# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = {"teda": "safdsa"}
b = a.setdefault("ted", {})  # 这里b其实是一个字典,只不过返回的是value
print(a)

dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

dict.setdefault('runoob', None)
dict.setdefault('Taobao', '淘宝')
print(dict)  # setdefault如果key不存在,那么会在原有的字典中添加此key及默认值

print("*********************************************")

"""
str.split(str="", num=string.count(str))
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
"""
info1 = '1.2.3.4.5'
info2 = 'a.b.c.d.f'

print(info1.split(".", 1))  # ['1', '2.3.4.5']


def transfer_kwargs(*args):
    kwargs = {}
    for arg in args:
        k, v = map(lambda x: x.strip(), arg.split('.', 1))  # 1 2.3.4.5
        if '.' in v:
            item = kwargs.setdefault(k, {})  # item={}, kwargs={'1': {}}
            values = v.split('.')  # ['2', '3', '4', '5']
            for j in values[:-2]:  # 把最后两位切掉了: ['2', '3']
                item = item.setdefault(j, {})  # step2
            item[values[-2]] = values[-1]  # step3
        else:
            kwargs.update({k: v})
    return kwargs


res = transfer_kwargs(info1, info2)
print(res)  # {'1': {'2': {'3': {'4': '5'}}}, 'a': {'b': {'c': {'d': 'f'}}}}

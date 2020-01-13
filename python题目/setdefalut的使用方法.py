# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = {"teda": "safdsa"}
b = a.setdefault("ted", {})  # 这里b其实是一个字典,只不过返回的是value
print(a)
b.update({"ted": 2})
print(a)

dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

print("Value : %s" % dict.setdefault('runoob', None))
print("Value : %s" % dict.setdefault('Taobao', '淘宝'))

print(dict)  # setdefault如果key不存在,那么会在原有的字典中添加此key及默认值

print("*********************************************")

info1 = '1.2.3.4.5'
info2 = 'a.b.c.d.f'


def transfer_kwargs(*args):
    kwargs = {}
    for arg in args:
        k, v = map(lambda x: x.strip(), arg.split('.', 1))
        print(k, v)
        if '.' in v:
            item = kwargs.setdefault(k, {})  # step1
            values = v.split('.')
            print("v:", values)
            for j in values[:-2]:
                item = item.setdefault(j, {})  # step2
            item[values[-2]] = values[-1]  # step3
        else:
            kwargs.update({k: v})
    print(kwargs)


transfer_kwargs(info1, info2)
# {'1': {'2': {'3': {'4': '5'}}}, 'a': {'b': {'c': {'d': 'f'}}}}

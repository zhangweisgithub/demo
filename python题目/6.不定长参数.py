# !/usr/bin/env python
# -*- coding: utf-8 -*-


def func(*args, **kwargs):
    for k,v in kwargs.items():
        print("key:{0}".format(k), "value:{0}".format(v))


func("12", name="zhangwei", age=12)


"""
range(100)
python2返回的是列表,python3返回的是迭代器,节约内存
"""






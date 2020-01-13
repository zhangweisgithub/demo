# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。

引用计数算法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，
变为1，如果再调用1次del，此时会真的把对象进行删除
"""
import time


class Animal(object):
    def __init__(self, name):
        print("__init__方法别调用")
        self.__name = name

    def __del__(self):
        print("__del__:对象真正被删除的时候调用!")


cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print(id(cat), id(cat2), id(cat3))
print("马上删除cat对象")
del cat
print("马上删除cat2对象")
del cat2
print("马上删除cat3对象")
del cat3
print ("程序在2秒钟之后结束")
time.sleep(2)












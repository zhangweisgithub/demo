# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python中的函数（function）与方法（method）的区别
https://blog.csdn.net/qq_44614026/article/details/108610467

"""

import inspect


def test1():
    print('这是方法还是函数？')


print(inspect.isfunction(test1))  # True
print(inspect.ismethod(test1))  # False

# 注意：不能用这种方式，这种方式会调用函数

import inspect


def test1():
    print('这是方法还是函数？')


print(inspect.isfunction(test1()))

# 输出结果  False

"""
非用户定义的函数，即内置函数，在 isfunction() 眼里并不是“函数”（FunctionType）！
"""
print("----------------")

import inspect

print(inspect.isfunction(len))  # False

print(inspect.isfunction(range))  # False
print(type(len))

# 输出结果： <class 'builtin_function_or_method'>

print("---------------")

"""一个类的静态方法，在 ismethod() 眼里并不是方法（MethodType）！"""


class MyTest():

    @classmethod
    def cls_func(cls):
        pass

    def ins_func(self):
        pass

    @staticmethod
    def sta_func():
        pass


print(inspect.ismethod(MyTest.cls_func))  # True
print(inspect.ismethod(MyTest.ins_func))  # False
print(inspect.ismethod(MyTest.sta_func))  # False

print(type(MyTest.cls_func))
print(type(MyTest.ins_func))

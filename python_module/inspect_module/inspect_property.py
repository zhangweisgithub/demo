# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。

2. 什么是callable
一个可callable的对象是指可以被调用执行的对象，并且可以传入参数， 用另一个简单的描述方式，
只要可以在一个对象的后面使用小括号来执行代码，那么这个对象就是callable对象，下面列举callable对象的种类
"""
import inspect


class Test(object):
    @property
    def get_name(self):
        return "Name is LiHua"

    @staticmethod
    def get_age(age=18):
        return age


print(inspect.getfullargspec(Test.get_age))
try:
    print(inspect.getfullargspec(Test.get_name))  # 可以在源码中看到,调用这个获取参数的话, 函数必须callable
except TypeError as e:
    print("类型错误")

print(inspect.isfunction(Test.get_age))
print(inspect.isclass(Test))
print(type(Test.get_name))
print(type(Test))
print(type(Test.get_age))

test = Test()
age = test.get_age(16)
print("年龄:", age)
name = test.get_name
print("名字:", name)

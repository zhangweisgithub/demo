# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自省是指这种能力：检查某些事物以确定它是什么、它知道什么以及它能做什么。自省向程序员提供了极大的灵活性和控制力。
   自省就是面向对象的语言所写的程序在运行时，能够知道对象的类型。简单一句就是，运行时能够获知对象的类型。
   Python中比较常见的自省（introspection）机制(函数用法)有： dir()，type(), hasattr(), isinstance()，
   通过这些函数，我们能够在程序运行时得知对象的类型，判断对象是否存在某个属性，访问对象的属性。
https://www.cnblogs.com/ArsenalfanInECNU/p/9110262.html
"""

import sys  # 模块，sys指向这个模块对象
import inspect


def foo():
    pass  # 函数，foo指向这个函数对象


class Cat(object):  # 类，Cat指向这个类对象
    def __init__(self, name=' kitty '):
        self.name = name

    def sayHi(self):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print(self.name, ' says Hi! ')  # 访问名为name的字段，使用实例.name访问


cat = Cat()  # cat是Cat类的实例对象

print(Cat.sayHi)  # 使用类名访问实例方法时，方法是未绑定的(unbound)
print(cat.sayHi)  # 使用实例访问实例方法时，方法是绑定的(bound)
print("---------")
cat = Cat('kitty')
print(cat.name)  # 访问实例属性 cat.sayHi()  #  调用实例方法
# dir(): 返回模块的属性列表。
print(dir(cat))  # 获取实例的属性名，以列表形式返回
if hasattr(cat, "name"):  # 检查实例是否有这个属性
    setattr(cat, "name", "tiger")  # same as: a.name = 'tiger'
print(getattr(cat, "name"))  # same as: print a.name
getattr(cat, "sayHi")()  # same as: cat.sayHi()

"""inspect:检查       自省模块:比如用来判断一个对象是否是函数等"""
print("---------")
im = cat.sayHi
if inspect.isroutine(im):
    im()

print(callable(foo))  # 判断一个函数是否能被调用

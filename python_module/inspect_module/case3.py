# !/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

"""
获取类的继承关系
Python 为所有类都提供了一个 bases 属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。注意是直接父类！！！
"""


class Rand(object):
    """
    doc内容
    """
    pass


class Animal(Rand):
    pass


print(inspect.getmro(Animal))
print(Animal.mro())
print(Animal.__mro__)
print(Animal.__name__)
print(Animal.__mro__[0].__bases__)
print(Animal.__mro__[0].__bases__[0].__name__)
print(Animal.__mro__[0].__dict__.items())
"""
(<class '__main__.Animal'>, <class '__main__.Rand'>, <class 'object'>)
[<class '__main__.Animal'>, <class '__main__.Rand'>, <class 'object'>]
(<class '__main__.Animal'>, <class '__main__.Rand'>, <class 'object'>)
Animal
(<class '__main__.Rand'>,)
Rand
dict_items([('__module__', '__main__'), ('__doc__', None)])
"""

print("--------------------------------------------")


def cat(host, passwd=None, user="root"):
    pass


func_input_args = inspect.getfullargspec(cat)
print(func_input_args)
arg_name_list = list(func_input_args.args)
print(arg_name_list)
"""
FullArgSpec(args=['host', 'passwd', 'user'], varargs=None, varkw=None, defaults=(None, 'root'), kwonlyargs=[], kwonlydefaults=None, annotations={})
['host', 'passwd', 'user']
"""

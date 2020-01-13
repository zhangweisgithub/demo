# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
写一个单列模式:
因为创建对象时__new__方法执行，并且必须return 返回实例化出来的对象所cls.__instance是否存在，不存在的话就创建对象，
存在的话就返回该对象，来保证只有一个实例对象存在（单列），打印ID，值一样，说明对象同一个
"""


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton(18, "dongge")
b = Singleton(12, "dongge")

print(id(a))
print(id(b))

a.age = 19          # 给a指向的对象添加一个属性
print(b.age)        # 获取b指向的对象的age属性

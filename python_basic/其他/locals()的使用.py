# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
locals() 函数会以字典类型返回当前位置的全部局部变量。

对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
"""


def runoob(arg):
    z = 1
    print(locals())


runoob(4)           # {'arg': 4, 'z': 1}

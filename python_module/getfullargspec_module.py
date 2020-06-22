# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
比较底层的模块
getfullargspec可以获取函数、方法定义了什么参数
"""

from inspect import getfullargspec


class A:
    def __init__(self, a, b, *args1, c, d=20, **kwargs1) -> None:
        ...


def test(host, username, passwd):
    print(host, username, passwd)


print(getfullargspec(A.__init__))
print(getfullargspec(test))
print(getfullargspec(test).args)

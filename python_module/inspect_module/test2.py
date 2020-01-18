# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__doc__用例访问模块,类声明或者函数的声明中第一个未被赋值的字符串
"""


class A():
    """123"""
    pass


print(A().__doc__)         # 123

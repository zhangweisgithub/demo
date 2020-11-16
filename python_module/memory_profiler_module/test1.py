# !/usr/bin/env python
# -*- coding: utf-8 -*-
from memory_profiler import profile

"""
分析空间耗时
https://www.cnblogs.com/2020-zhy-jzoj/p/13164788.html
"""

@profile
def operation1():
    num = 0
    for i in range(10000):
        num += 1


@profile
def operation2():
    num = 0
    while (num < 10000):
        num += 1


if __name__ == "__main__":
    operation1()
    operation2()

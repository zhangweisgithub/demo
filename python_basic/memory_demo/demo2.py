# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
基于磁盘的缓存   joblib
教程 https://joblib.readthedocs.io/en/latest/memory.html
安装 pip install joblib
"""

from joblib import Memory

memory = Memory(location="./cachedir")


@memory.cache
def sum2(a, b):
    print(f"计算{a}+{b} ... ")
    return a + b


print(sum2(2, 3))
print(sum2(2, 3))

print(sum2(4, 7))
print(sum2(4, 7))

print(sum2(2, 3))
print(sum2(4, 7))


"""
后续的计算直接从磁盘的缓存中进行读取了,就不走这个函数了
"""

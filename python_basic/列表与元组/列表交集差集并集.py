# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
如果使用set中的函数,需要把列表先转换为集合
"""
a = [1, 2, 3, 4]
b = [4, 3, 5, 6]
jj1 = [i for i in a if i in b]
jj2 = list(set(a).intersection(set(b)))         # 交集
print(jj1)
print(jj2)


bj1 = list(set(a).union(set(b)))             # 并集
print(bj1)


# 求差集
cj1 = list(set(a).difference(set(b)))           # a中有b中没有       非常高效
cj2 = list(set(b).difference(set(a)))           # b中有a中没有

print(cj1)
print(cj2)



















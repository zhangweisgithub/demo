# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
列表可以跟元组字典相互转换
字典转换为列表相当于把字典中对应的key值放在列表中
"""
a = {"a": "b", "c": "d", 1: 2}
print(list(a))  # ['a', 'c', 1]

d = {"a": "b", "c": "d", 1: 2}
print(tuple(a))  # ('a', 'c', 1)

b = ["a", "b"]
print(tuple(b))  # ('a', 'b')

c = ('a', 'b')
print(list(c))  # ['a', 'b']

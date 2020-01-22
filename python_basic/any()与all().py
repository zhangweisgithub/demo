# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真
python中什么元素为假？
答案：（0，空字符串，空列表、空字典、空元组、None, False）
"""
print(bool(()))
print(bool({}))
print(bool(""))

a = [True, False]
print(any(a))          # True
print(all(a))          # False

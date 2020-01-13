# !/usr/bin/env python
# -*- coding: utf-8 -*-

print("********************我是分割线*********************")
"""
python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
"""

s = divmod(7, 2)
print(s)  # (3, 1)
s2 = divmod(8, 2)
print(s2)  # (4, 0)

"""insert() 函数用于将指定对象插入列表的指定位置。"""
alist = [123, "xyz", "abc", "test"]
alist.insert(3, 2014)
print(alist)  # [123, 'xyz', 'abc', 2014, 'test']

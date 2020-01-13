# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。
zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组
"""

a = [1, 2]
b = [3, 4]
res = [i for i in zip(a, b)]
print(res)                # [(1, 3), (2, 4)]

c = (1, 2)
d = (3, 4)
res2 = [i for i in zip(c, d)]
print(res2)            # [(1, 3), (2, 4)]

e = "as"
f = "opd"
res3 = [i for i in zip(e, f)]
print(res3)              # [('a', 'o'), ('s', 'p')]


















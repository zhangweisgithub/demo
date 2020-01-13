# !/usr/bin/env python
# -*- coding: utf-8 -*-
list1 = [12, 12, 13, 14, 15, 16, 18, 15]
a = set(list1)
print(a)  # set([12, 13, 14, 15, 16, 18])
# print(list(a))      # [12, 13, 14, 15, 16, 18]:先通过集合去重,在转换为列表
print([x for x in a])

list2 = [(12,), (13,), (12,), (13,), (12,), (15,), (12,), (15,)]
print(list(set([x[0] for x in list2])))

"""列表相加:等价于extend"""
m = [1, 2, 3]
n = [3, 5, 6]
res = m + n
print("列表相加:", res)  # 列表相加: [1, 2, 3, 3, 5, 6]

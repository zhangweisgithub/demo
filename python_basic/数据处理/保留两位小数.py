# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = "%.03f" % 1.335
print(a, type(a))
b = round(float(a), 1)  # round:圆形的,这里表示四舍五入,保留一位小数
print(b)
c = round(float(a), 2)
print(c)

A = zip(("a", "b"), (1, 2, 3))
print(A)  # [('a', 1), ('b', 2)]
print(dict(A))  # {'a': 1, 'b': 2})


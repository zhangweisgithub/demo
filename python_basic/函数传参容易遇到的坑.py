# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 函数的参数只有在首次执行的时候会进行初始化


def get_target(a, b=[]):
    b.append(a)
    print(b)


get_target(1)  # [1]
get_target(2)  # [1, 2]

print("_______________________________")


def f(a, t=None):
    t = t or []  # 这个地方的意思是如果有t那么就是t,如果没有t,那么就是None
    t.append(a)
    return t


for i in range(3):
    print(f(i, [32]))

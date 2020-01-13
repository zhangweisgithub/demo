# !/usr/bin/env python
# -*- coding: utf-8 -*-


def test(a, b, c=3, *args):
    print(a)
    print(b)
    print(c)
    print(args)


test(11, 22, 33, 44, 55)  # 多出来的参数已元组的形式进行保存
print("*******************************")


def test(a, b, c=3, *args1, **args2):
    print(a)
    print(b)
    print(c)
    print(args1)
    print(args2)


test(11, 22, 33, 1, 2, 3, dd=44, ee=55, ff=66)  # 多出来的参数以字典的形式保存

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 匿名函数实现两个数的相称
sum = lambda a, b: a * b
print(sum(4, 5))

# 一个整数数列,要求按照列表中绝对值的大小升序排列
list1 = [3, 5, -4, 0, -1, 6]
print(sorted(list1, key=lambda x: abs(x)))

# 排序函数sorted支持接收一个函数作为参数,改参数作为sorted的排序依据,这里按照列表的元素值进行排序

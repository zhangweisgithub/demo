# -*- coding: utf-8 -*-
# @Time    : 2018-05-03 9:24
# @Email   : Yzh_smlie@163.com
# @File    : 求1-100和.py

# 第一种方法
a = 0
for i in range(0, 100):
    a += (i + 1)
print(a)

# 第二种方法
print(sum(range(1, 101)))

##第三种方法
print(sum([x for x in range(0, 101)]))

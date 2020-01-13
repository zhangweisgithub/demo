# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 18:31
# @Email   : Yzh_smlie@163.com
# @File    : 修改函数内全局变量.py

a = 5

def fn():
    global a
    a = 4


print(fn())
print(a)
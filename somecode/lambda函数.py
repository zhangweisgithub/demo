# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 20:29
# @Email   : Yzh_smlie@163.com
# @File    : lambda函数.py

# lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数

a = map(lambda x: x * 2, [1, 2, 3])
# print(list(a))

sum = lambda a, b: a * b
print(sum(5, 4))

'''
1、lambda函数比较轻便，即用即仍，很适合需要完成一项功能，但是此功能只在此一处使用，连名字都很随意的情况下；

2、匿名函数，一般用来给filter，map这样的函数式编程服务;

3、作为回调函数，传递给某些应用，比如消息处理
'''
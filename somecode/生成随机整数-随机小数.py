# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 19:54
# @Email   : Yzh_smlie@163.com
# @File    : 生成随机整数-随机小数.py

'''
随机整数：random.randint(a,b),生成区间内的整数
随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
0-1随机小数：random.random(),括号中不传参
'''
import random
import numpy

result = random.randint(10,20)
res = numpy.random.randn(5)
ret = random.random()

print('正整数',result)
print('5个随机小数',res)
print('0-1随机小数',ret)
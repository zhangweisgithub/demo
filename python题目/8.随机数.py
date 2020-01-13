# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy
result = random.randint(10, 20)
print(result)

"""
NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
"""
# 随机小数，序贯用numpy库,利用np.random.randn(5),生成5个随机小数
# 0-1随机小数:random.random(),括号中不传参

res = numpy.random.randn(5)
print(res)

ret = random.random()     # 不能传参
print(ret)







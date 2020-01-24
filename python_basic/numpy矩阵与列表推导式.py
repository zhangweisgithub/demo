# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 一行代码展开列表,得到[1,2,3,4,5,6]
a = [[1, 2], [3, 4], [5, 6]]
x = [j for i in a for j in i]
print("方法一:", x)  # [1, 2, 3, 4, 5, 6]

"""骚方法:还可以将列表转换为numpy矩阵,通过numpy的flatten()方法"""
import numpy as np

b = np.array(a).flatten().tolist()
print("方法二:", b)


"""
flatten:变平，使（某物）变平； 打倒，击倒； 使失去光泽；
v是一个矩阵或者数组,v.flatten()就是把v降到一维,默认是按横的方向降
"""
v = np.array([[1, 2], [3, 4], [5, 6]])  # 形成一个矩阵
print(v)
"""
[[1 2]
 [3 4]
 [5 6]]
"""
# flatten函数可以实现降维
print(v.flatten())  # 默认按照横向:[1 2 3 4 5 6]
print(v.flatten('F'))  # 按竖的方向  : [1 3 5 2 4 6]

# 试一下元组
m = [(1, 2), (3, 4)]
n = np.array(m).flatten("F")
print(n)  # 元组也是可以实现的

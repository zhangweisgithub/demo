# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 20:59
# @Email   : Yzh_smlie@163.com
# @File    : 列表推导式.py

# 列表推导式求列表所有奇数并构造新列表，
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i % 2 == 1]
print(res)

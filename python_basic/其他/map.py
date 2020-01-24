# -*- coding: utf-8 -*-
# @Time    : 2018-04-28 10:32
# @Email   : Yzh_smlie@163.com
# @File    : map.py

a = map(lambda x: x * 2, [1, 2, 3])
print(list(a))

# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，
# 并使用列表推导式提取出大于10的数，
# 最终输出[16,25]
list = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


"""
map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写
在python3.0中，map会先输入一个函数参数，以及一个或多个序列参数，然后用从序列中取出的并行元素来调整，最后把结果收集起来并返回
（map是一个值生成器，必须传入list从而一次性收集并显示其结果），返回的是迭代器
"""
res = map(fn, list)  # 返回一个迭代器:<map object at 0x0000024722D1E400>
res = [i for i in res if i > 10]
print(res)

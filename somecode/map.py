# -*- coding: utf-8 -*-
# @Time    : 2018-04-28 10:32
# @Email   : Yzh_smlie@163.com
# @File    : map.py

a = map(lambda x: x * 2, [1, 2, 3])
# print(list(a))

# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，
# 并使用列表推导式提取出大于10的数，
# 最终输出[16,25]
# map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写
list = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


res = map(fn, list)
res = [i for i in res if i > 10]
print(res)

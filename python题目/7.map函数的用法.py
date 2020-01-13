# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
"""
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


res = map(func, list1)
res = [i for i in res if i > 10]
print(res)

# 匿名函数可以使函数更加简化
a = ["苏州", "中国", "哈哈", "", "", "日本", "", "德国"]
res = list(map(lambda x: "填充值" if x == "" else x, a))
print(res)

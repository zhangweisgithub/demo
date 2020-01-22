# !/usr/bin/env python
# -*- coding: utf-8 -*-

# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# 利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作

list1 = [2, 3, 5, 4, 9, 6]
new_list = []


def get_min(list1):
    a = min(list1)
    list1.remove(a)
    new_list.append(a)
    if len(list1) > 0:
        get_min(list1)
    return new_list


res = get_min(list1)
print(res)

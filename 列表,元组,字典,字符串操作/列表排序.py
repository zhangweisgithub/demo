# !/usr/bin/env python
# -*- coding: utf-8 -*-

# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# 利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作

list = [2, 3, 5, 4, 9, 6]
new_list = []


def get_min(list):
    a = min(list)
    list.remove(a)
    new_list.append(a)
    if len(list) > 0:
        get_min(list)
    return new_list


new_list = get_min(list)
print new_list









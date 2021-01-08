# !/usr/bin/env python
# -*- coding: utf-8 -*-


def seprate_list_with_length(one_list, c=3):
    """
    将一个长度为n的列表划分 ，每个子列表中包含m个元素
    """
    return [one_list[i:i + c] for i in range(len(one_list)) if i % c == 0]


print(seprate_list_with_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5))

"""
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12]]
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
基本思想: 冒泡排序，类似于水中冒泡，较大的数沉下去，较小的数慢慢冒起来，假设从小到大，即为较大的数慢慢往后排，较小的数慢慢往前排。
直观表达，每一趟遍历，将一个最大的数移到序列末

冒泡排序的时间复杂度是O(N^2)
冒泡排序的思想: 每次比较两个相邻的元素, 如果他们的顺序错误就把他们交换位置
冒泡排序原理: 每一趟只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位, 也就是说要进行n-1趟操作(已经归位的数不用再比较)
缺点: 冒泡排序解决了桶排序浪费空间的问题, 但是冒泡排序的效率特别低
"""


def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):  # 从大到小排列
        # j表示每次遍历需要比较的次数,是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


li = [54, 15, 12, -10, 45, 96, 23, 75]
bubble_sort(li)
print(li)  # [-10, 12, 15, 23, 45, 54, 75, 96]


# 第二种方法:
def bubble_sort2(lis):
    for i in range(0, len(lis)):
        for j in range(i + 1, len(lis)):  # 这个代表随着i的增加,进行比较的次数会越来越少
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis


print(bubble_sort2(li))

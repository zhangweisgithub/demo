# !/usr/bin/env python
# -*- coding: utf-8 -*-

# range(start, stop[, step])
print(list(range(5)))        # [0, 1, 2, 3, 4]   默认是0-4
print(list(range(0, 5)))        # [0, 1, 2, 3, 4]

print(list(range(1, 7)))        # [1, 2, 3, 4, 5, 6]

# print(list(range(3, 20, 3)))        # [3, 6, 9, 12, 15, 18]   第三个参数代表的是step

print(list(range(10, 0, -1)))          # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 代表的是从大到小排列,range的第一个参数大于第二个,step必须为负


for i in range(10, 0, -1):
    print(i)

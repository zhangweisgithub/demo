# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
for 循环中如果remove掉一个数据,那么其后的一个数据不会再下次的遍历中被遍历到
"""
a = [11,22,33,44,55,66]
# for i in a:
#     if i==33 or i==44:
#         a.remove(i)
# print(a)
#
b = []
for i in a:
    if i == 33 or i == 44:
        b.append(i)
for m in b:
    a.remove(m)
print(a)


"""解决方法:"""
a = [1, 2, 3, 4, 5]
b = []
print(a[:])
for i in a[:]:
    if i == 1:
        a.remove(i)
        continue
    b.append(i)
print(b)

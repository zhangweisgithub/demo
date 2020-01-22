# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
for 循环中如果remove掉一个数据,那么其后的一个数据不会再下次的遍历中被遍历到(后面数据的索引值会发生变化)
"""
a = [11, 22, 33, 44, 55, 66]
for i in a:
    if i == 33 or i == 44:
        a.remove(i)
print(a)

"""解决方法:"""
for i in a[:]:  # 相当于遍历了a所构造的一个新列表
    if i == 33 or i == 44:
        a.remove(i)
print(a)

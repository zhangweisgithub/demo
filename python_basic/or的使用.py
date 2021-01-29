# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
or使用的小技巧
为None或0或 "" 返回or后面的
"""
a = 0
b = 2
c = a or b

print(c)

a = 0
b = None
c = a or b

print(c)

a = ""
b = None
c = a or b

print(c)

print(dict({}))

print("---------------")
"""
如果_list为空的话,就便利or后面的数据
"""
_list = [2, 3]
for item in _list or (1, 2):
    print(item)

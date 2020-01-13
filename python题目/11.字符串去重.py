# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""字符串去重并排序,可以先转换为列表,然后排序,最后列表中的元素进行合并"""
s = "afdsafwfwfasdfasf"
s = list(set(s))            # ['a', 's', 'd', 'w', 'f']
s.sort(reverse=False)
res = "".join(s)            # 对列表中的元素进行合并,形成字符串
print(res)















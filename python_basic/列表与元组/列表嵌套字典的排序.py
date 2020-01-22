# !/usr/bin/env python
# -*- coding: utf-8 -*-
foo = [{"name": "sz", "age": 12}, {"name": "xian", "age": 13}]
a = sorted(foo, key=lambda x: x["age"], reverse=False)  # 年龄从大到小
print(a)

foo = [("xge", 12), ("ge", 13), ("sge", 13)]
d = sorted(foo, key=lambda x: (x[1], x[0]), reverse=False)  # 年龄相同的话,添加参数,按照字母进行排序
print(d)

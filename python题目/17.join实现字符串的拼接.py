# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""join()括号里的是可迭代对象,x插入可迭代对象中间,形成字符串"""
x = "abc"
y = "123"
z = ["$", "%", "@"]

m = x.join(y)
n = x.join(z)
print(m)             # 1abc2abc3
print(n)             # $abc%abc@



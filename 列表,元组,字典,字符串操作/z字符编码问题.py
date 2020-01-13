# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = [u"\u4fdd\u5b58\u9879", u"\u6d4b\u8bd5"]
b = []
for i in a:
    print("1:", type(i))
    print("3;", i)
    i.encode("utf8")
    print i
    b.append(i)
print b
# a = u"\u4fdd\u5b58\u9879"
# b = a.encode("utf8")
# print(b)


n = u'\u4fdd\u5b58\u9879'
n.encode("utf8")
print(n)
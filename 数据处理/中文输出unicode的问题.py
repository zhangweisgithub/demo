# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
a = '["\u4fdd\u5b58\u9879", "\u6d4b\u8bd5"]'
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


"""python2中对字符的处理"""
print("-----------------------")
p = u'["\u6211\u662f", "\u6d4b\u8bd5", "\u7684\u6d4b\u8bd5\u9898"]'
q = json.dumps(p, ensure_ascii=False)
print q                 #  "[\"我是\", \"测试\", \"的测试题\"]"

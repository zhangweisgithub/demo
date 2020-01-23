# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,}	匹配前一个字符至少出现m次
{m,n}	匹配前一个字符出现从m到n次
"""


import re

ret = re.match("[A-Z][a-z]*","Mm")
ret.group()
print(ret.group())       # Mm

ret = re.match("[A-Z][a-z]*","Aabcdef")
ret.group()
print(ret.group())          # Aabcdef

print("--------------------")

ret = re.match("[a-zA-Z_]+[\w_]*","name1")
ret.group()
print(ret.group())

ret = re.match("[a-zA-Z_]+[\w_]*","_name")
ret.group()
print(ret.group())

ret = re.match("[a-zA-Z_]+[\w_]*","b2_name")
ret.group()
print(ret.group())

print("--------------")

ret = re.match("[1-9]?[0-9]","7")
ret.group()
print(ret.group())

ret = re.match("[1-9]?[0-9]","33")
ret.group()
print(ret.group())

ret = re.match("[1-9]?[0-9]","09")
ret.group()
print(ret.group())









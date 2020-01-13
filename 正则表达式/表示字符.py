# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符	功能
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符
"""

import re

ret = re.match(".", "a")
ret.group()
print(ret.group())
ret = re.match(".", "b")
ret.group()
print(ret.group())
ret = re.match(".", "M")
ret.group()
print(ret.group())



import re

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h","hello Python")
ret.group()
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H","Hello Python")
ret.group()
print(ret.group())

# 大小写h都可以的情况
print("--------")
ret = re.match("[hH]","hello Python")
ret.group()
print(ret.group())
ret = re.match("[hH]","Hello Python")
ret.group()
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]","7Hello Python")
ret.group()
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]","7Hello Python")
ret.group()
print(ret.group())


print("-----------------")
# 普通的匹配方式
ret = re.match("嫦娥1号","嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥2号","嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥3号","嫦娥3号发射成功")
print(ret.group())

# 使用\d进行匹配
ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号","嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号","嫦娥3号发射成功")
print(ret.group())
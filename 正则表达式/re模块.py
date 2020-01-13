# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
re.match() 能够匹配出以xxx开头的字符串
re.match(正则表达式,要匹配的字符串)
可以判断这个字符串中是否有某个规则下的字符
"""
import re

result = re.match("itcast", "itcast.cn")
if result:
    result.group()
    print(result.group())




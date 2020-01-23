# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
判断装饰器是否被注释掉
"""
import re
a = "# @flow"
c = re.compile(r'#\s*@flow$')
b = c.findall(a)
print(b)

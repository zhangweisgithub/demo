# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""在python3中运行,否者字符编码会出现问题"""
import re

title = "你好 hello, 世界"
pattern = re.compile(r"[\u4e00-\u9fa5]+")   # 匹配一个或多个中文
result = pattern.findall(title)
print(result)



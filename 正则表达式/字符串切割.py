# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
|表示或，根据冒号或者空格切分
"""
import re

s = "info:xiaozhang 33 shandong"
res = re.split(r":| ", s)
print(res)








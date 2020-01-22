# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""生成符合正则表达式的字符串"""
import sys
from xeger import Xeger

_x = Xeger(limit=4)
out = _x.xeger(r"[A-Z]\d[A-Z]")
print(out)  # A5G:这个就是随机生成的服务上面正则表达式的字符串


print(sys.maxsize)       # 9223372036854775807
xe = Xeger(limit=sys.maxsize)
bucket_name = xe.xeger("^[A-Za-z0-9]{3,64}$")
print(bucket_name)
print(len(bucket_name))  # 存储空间的命名规范:bucket的长度为3-64位,只能包括小写字母,数字和短横线

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""osmknod直接创建一个文件"""

# import os
# file = "test.txt"
# if not os.path.exists(file):
#     file = open(file, "w")
#     file.write("hello")
import re
import ast
a = "293bef-5454-asf58afs-110"
print(type(a))

if re.match("^[\d]+$", a):
    print("reasf")
else:
    raise IOError("文件不存在")

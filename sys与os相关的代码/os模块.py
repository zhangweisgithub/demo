# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
"""
会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，会从”./”开头的参数的上一个参数开始拼接。
"""
print("1:", os.path.join("aaa", "/bbb", "ccc.txt"))
print("2:", os.path.join("/aaa", "/bbb", "/ccc.txt"))
print("3:", os.path.join("aaa", "./bbb", "ccc.txt"))


# 在python2中,print是一种输出语句    print  heh
# 在python3中,print()是一个函数,通过格式化函数format()来控制输出格式


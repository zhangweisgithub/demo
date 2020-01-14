# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
try:
    正常的操作
except:
    发生异常,执行这块的代码
else:
    如果没有异常,执行这块代码
finally:
    退出try时总会执行这行代码
"""

from datetime import datetime

try:
    fh = open("test.log", "a+", encoding="utf-8")
    try:
        fh.write("这是一个测试文件,用于测试异常\n")
    finally:
        print(str(datetime.now()) + "--" + "关闭文件")
        fh.close()
except IOError:
    print("Error:,没有找到文件或读取文件失败")
else:
    print("有没有发生任何异常")

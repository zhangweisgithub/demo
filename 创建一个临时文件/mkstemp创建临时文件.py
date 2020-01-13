# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import os

"""mkstemp会在路径中创建一个文件"""
_, temp_path = tempfile.mkstemp(prefix="temp", suffix=".py", dir=os.path.dirname(__name__), text=False)
print(_)
print(temp_path)
with open(temp_path, "w+") as fd:
    fd.write("我是临时文件")
    # fd.seek(0)
    # print(fd.read())
import time
time.sleep(1)
# os.close(_)
try:
    os.remove(temp_path)
except Exception as e:
    print(e)
"""
[WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'C:\\Users\\ZHANGW~1\\AppData\\Local\\Temp\\tempgxwgbg7w.py'
"""

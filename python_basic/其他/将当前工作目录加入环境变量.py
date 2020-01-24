# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ["HOME_PATH"] = os.path.split(os.path.realpath(__file__))[0]
print("1:", os.path.realpath(__file__))          # D:\project\demo\文件处理\获取路径下所有的py文件.py
print(os.environ["HOME_PATH"])                   # D:\project\demo\文件处理

test = os.path.join(os.environ["HOME_PATH"], "test.py")       # D:\project\demo\文件处理\test.py


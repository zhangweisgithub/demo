# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python执行py文件的时候,会默认把当前的目录增加的sys.path中
"""
import os

print(__file__)  # D:/platform/demo/somecode/__file__打印文件当前位置.py
print(os.path.dirname(__file__))  # D:/project/demo/somecode 会打印当前文件所在的文件夹路径

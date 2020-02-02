# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python执行py文件的时候,会默认把当前的目录增加的sys.path中
"""
import os

print(__file__)  # D:/project/demo/python_basic/魔法方法相关/__file__方法.py
print(os.path.dirname(__file__))  # D:/project/demo/python_basic/魔法方法相关

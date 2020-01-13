# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""python动态导入对象:一个函数运行根据不同的配置,动态导入对应的配置文件运行"""

# 比如我现在需要导入distinct中的所有对象
import importlib
print(__file__)     # C:/zhangwei_vendor/����/code/importlib.import_model.py
print(__name__)     # __main__
# 每个对象都会有一个__doc__属性，用于描述该对象的作用
print(__doc__)      # python动态导入对象:一个函数运行根据不同的配置,动态导入对应的配置文件运行
params = importlib.import_module("distinct", package="code")          # 绝对路径导入
# params = importlib.import_module('.distinct', package="code")

print(params)

"""
['hello', 'world', ['wode', 'asfd'], 'hello', 'python']
['hello', 'world', ['asf', 'asfd'], 'hello', 'python']
<type 'unicode'>
True
%name%:zhangwei
<module 'distinct' from 'C:\zhangwei_vendor\����\code\distinct.pyc'>
"""

# 当args中的数据发生变化的时候,这里取出的数据也会跟着发生更改
print (params.args)          # 取出变量:{'a': 1}
params.C                    # 取出class C
params.C.c                  # 取出class C中的c 方法







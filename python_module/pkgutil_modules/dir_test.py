# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import python_module
from python_module.pkgutil_modules.clazz import a

print(dir(a))             # 获得当前模块的属性列表

"""
想要获取到a中所包含的方法,可以使用dir函数
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'showa']
"""
print(dir(python_module.pkgutil_modules.clazz))

"""
要获取包中所有的模块,直接使用dir并没有获取到
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a']
"""

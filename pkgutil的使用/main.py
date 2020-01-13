# !/usr/bin/env python
# -*- coding: utf-8 -*-

from pkgutil的使用.clazz import a

"""1、获取模块中的属性
想要获取clazz包中a模块的所包含的方法，可以直接使用dir这个函数，可以看到show 这个方法已经包含在其中
"""
print(dir(a))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'show']

"""
2、获取包中的属性
如果我要获取clazz 包中所有模块，直接使用dir 并没有获取
"""

import pkgutil的使用.clazz

print(dir(pkgutil的使用.clazz))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__path__', '__spec__']



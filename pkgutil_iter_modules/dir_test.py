# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgutil_iter_modules.clazz import a

print(dir(a))

"""
想要获取到a中所包含的方法,可以使用dir函数
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'showa']
"""

import pkgutil_iter_modules

print(dir(pkgutil_iter_modules.clazz))

"""
要获取包中所有的模块,直接使用dir并没有获取到
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a']
"""

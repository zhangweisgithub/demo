# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pkgutil
from pkgutil_iter_modules import clazz    # 导包的时候,如果clazz目录下没有__inti__文件,那么这个地方会报错,但不会影响程序的运行

print(clazz.__path__)       # __path__指定了包的搜索路径:_NamespacePath(['D:\\platform\\demo\\pkgutil_iter_modules\\clazz'])
print(clazz.__name__)       # pkgutil_iter_modules.clazz

for filefiner, name, ispkg in pkgutil.iter_modules(clazz.__path__, clazz.__name__ + "."):
    print("{0} name: {1}, is_sub_package: {2}".format(filefiner, name, ispkg))


"""
FileFinder('D:\\platform\\demo\\pkgutil_iter_modules\\clazz') name: pkgutil_iter_modules.clazz.a, is_sub_package: False
FileFinder('D:\\platform\\demo\\pkgutil_iter_modules\\clazz') name: pkgutil_iter_modules.clazz.b, is_sub_package: False
"""

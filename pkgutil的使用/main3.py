# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pkgutil, pkgutil的使用.clazz, importlib

"""
__path__指定了包的搜索路径
如果模块是被导入，__name__的值为模块名字
"""
module_list = []
for filefiner, name, ispkg in pkgutil.iter_modules(pkgutil的使用.clazz.__path__, pkgutil的使用.clazz.__name__ + "."):
    print(pkgutil的使用.clazz.__path__)
    print(pkgutil的使用.clazz.__name__ + ".")
    print(filefiner, name, ispkg)
    print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))

    module_list.append(importlib.import_module(name))
print("list:", module_list)

"""

['D:\\project\\demo\\pkgutil的使用\\clazz']
pkgutil的使用.clazz.
FileFinder('D:\\project\\demo\\pkgutil的使用\\clazz') pkgutil的使用.clazz.a False
FileFinder('D:\\project\\demo\\pkgutil的使用\\clazz') name: pkgutil的使用.clazz.a, is_sub_package: False\

['D:\\project\\demo\\pkgutil的使用\\clazz']
pkgutil的使用.clazz.
FileFinder('D:\\project\\demo\\pkgutil的使用\\clazz') pkgutil的使用.clazz.b False
FileFinder('D:\\project\\demo\\pkgutil的使用\\clazz') name: pkgutil的使用.clazz.b, is_sub_package: False
"""

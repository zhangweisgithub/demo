# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pkgutil
import importlib
import python_module.pkgutil_modules.clazz as clazz_module

"""
__path__指定了包的搜索路径
如果模块是被导入，__name__的值为模块名字
"""
module_list = []
for filefiner, name, ispkg in pkgutil.iter_modules(clazz_module.__path__, clazz_module.__name__ + "."):
    print(clazz_module.__path__)
    print(clazz_module.__name__ + ".")
    print(filefiner, name, ispkg)
    print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))

    module_list.append(importlib.import_module(name))
print("list:", module_list)

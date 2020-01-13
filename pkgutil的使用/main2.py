# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
既然，模块可以查看其中包含的属性，而包其实就是一个文件夹
那么，先获取包文件夹下的所有模块文件，再逐个导入模块，最后也可以获取模块中的属性
"""
import os
import importlib


def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)     # ['a.py', 'b.py', '__init__.py', '__pycache__']

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)            # a   .py
            modules.append("." + name)

    return modules


if __name__ == '__main__':
    package = "clazz"
    modules = get_modules(package)    # ['.a', '.b']

    # 将包下的所有模块，逐个导入，并调用其中的函数
    for module in modules:
        module = importlib.import_module(module, package)
        # <module 'clazz.a' from 'D:\\project\\demo\\pkgutil的使用\\clazz\\a.py'>

        for attr in dir(module):
            if not attr.startswith("__"):
                func = getattr(module, attr)     # getattr() 函数用于返回一个对象属性值
                print(func)                      # <function show at 0x000001D9951CBEA0>得到的是一个函数对象
                func()

    """
    show A
    show B
    """

"""
可以看到，我在只知道包名的情况下，成功获取了包下所有模块，和模块中所有的方法，并成功调用

注意，相对导入的时候需要在模块名前面加.

but!!!， python推荐使用pkgutil.iter_modules(path=None, prefix='')
"""



"""
import importlib

# 绝对导入
a = importlib.import_module("clazz.a")
a.show()
# show A

# 相对导入
b = importlib.import_module(".b", "clazz")
b.show()
"""
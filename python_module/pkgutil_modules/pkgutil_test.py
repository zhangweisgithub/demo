# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
既然，模块可以查看其中包含的属性，而包其实就是一个文件夹
那么，先获取包文件夹下的所有模块文件，再逐个导入模块，最后也可以获取模块中的属性。
"""

import os
import importlib


def get_modules(package="."):
    """获取包名下所有非__init__的模块名"""
    modules = []
    files = os.listdir(package)          # ['a.py', 'b.py', '__pycache__']    __pycache__ 里面存放的是编译好的字节码,cpu直接读取
    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)      # a, .py   分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
            modules.append("." + name)

    return modules                                          # [".a", ".b"]


if __name__ == '__main__':
    package = "clazz"
    modules = get_modules(package)

    # 将包下的所有模块，逐个导入，并调用其中的函数 (动态导入模块)
    for module in modules:                                  # 首先module=.a ,package=clazz
        module = importlib.import_module(module, package)   # <module 'clazz.a' from 'D:\\platform\\demo\\pkgutil_iter_modules\\clazz\\a.py'>

        for attr in dir(module):                       # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'showa']
            if not attr.startswith("__"):
                func = getattr(module, attr)           # <function showa at 0x000001D212333048>   得到的是一个函数,这样就可以通过这个函数访问它的属性了
                func()                                 # 这个地方执行了函数,所以会打印出函数对应的值

    """
    show A
    show B
    """


"""
可以看到，我在只知道包名的情况下，成功获取了包下所有模块，和模块中所有的方法，
并成功调用,但是python推荐使用pkgutil.iter_modules(path=None, prefix="")
"""

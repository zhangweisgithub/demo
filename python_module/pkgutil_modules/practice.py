# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import importlib


def get_modules(package="."):
    modules = []
    files = os.listdir(package)
    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append("." + name)
    return modules


if __name__ == '__main__':
    package = "clazz"
    modules = get_modules(package)
    for module in modules:
        module = importlib.import_module(module, package)     # 官方推荐的使用方法
        for attr in dir(module):
            if not attr.startswith("__"):
                func = getattr(module, attr)
                func()

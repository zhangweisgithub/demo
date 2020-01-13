# !/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib

# 绝对导入
a = importlib.import_module("clazz.a")
a.show()
# show A

# 相对导入
b = importlib.import_module(".b", "clazz")
b.show()
# show B

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import os
file_object = tempfile.TemporaryFile(dir=os.path.dirname(__file__))
print(file_object)
print(file_object.name)

with file_object as f:
    f.write(b"asfdafasdfasf")
    f.seek(0)   # 文件指针到文件的初始位置
    print(f.read())


'''
TemporaryFile类的构造方法，其返回的还是一个文件对象。但这个文件对象特殊的地方在于
1. 对应的文件没有文件名，对除了本程序之外的程序不可见
2. 在被关闭的同时被删除
所以上面的两句打印语句，输出分别是一个文件对象，以及一个<fdopen>（并不是文件名）
'''

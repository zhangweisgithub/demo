# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
copy与deepcopy:copy相当于第一层的copy,更深层次采用的是引用地址的方式,deepcopy相当于开辟了一个新的内存空间
"""
import copy

list1 = ["hello", "world", ["asf", "asfd"], "hello", "python"]
a = copy.copy(list1)   # ['hello', 'world', ['wode', 'asfd'], 'hello', 'python'] 2718133127688
b = copy.deepcopy(list1)  # ['hello', 'world', ['asf', 'asfd'], 'hello', 'python'] 2718133127624
print(a, id(a))
print(b, id(b))


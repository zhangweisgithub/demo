# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""反向生成符合正则表达式的字符串"""
import sys
from xeger import Xeger

_x = Xeger(limit=4)
out = _x.xeger(r"[A-Z]\d[A-Z]")
print (out)  # A5G

""" pdb相当于一个断点调试功能: pdb单步执行太麻烦了，所以第二种方法是import pdb 之后，直接在代码里需要调试的地方放一个pdb.set_trace()，
就可以设置一个断点， 程序会在pdb.set_trace()暂停并进入pdb调试环境，可以用pdb 变量名查看变量，或者c继续运行
修改下上面的实例如下，import pdb, 添加了pdb.set_trace()到可能出错的代码前面"""
import pdb
pdb.set_trace()

xe = Xeger(limit=sys.maxsize)
bucket_name = xe.xeger("^[A-Za-z0-9]{3,64}$")
print(bucket_name)
print(len(bucket_name))           # 存储空间的命名规范:bucket的长度为3-64位,只能包括小写字母,数字和短横线
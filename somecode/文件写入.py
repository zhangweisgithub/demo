# -*- coding: utf-8 -*-
# @Time    : 2018-05-06 14:20
# @Email   : Yzh_smlie@163.com
# @File    : 文件写入.py

# 写出一段代码打开一个名为user.log的文件，并写入 hello world
with open('user.log','w') as f:
    f.write("hello world")



# 文件删除
import os
os.remove('lvhao')
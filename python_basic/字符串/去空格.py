# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""方法1:替换"""
str = "  hello world hah hah "
res = str.replace(" ", "")
print(res)


"""方法2:切割"""
list = str.split(" ")  # ['hello', 'world', 'hah', 'hah', '']
res = "".join(list)
print(res)

"""方法3:首位去空格"""
print(str.strip())       # 去掉首位空格
print(str.lstrip())      # 去掉行首空格
print(str.rstrip())      # 去掉行尾空格

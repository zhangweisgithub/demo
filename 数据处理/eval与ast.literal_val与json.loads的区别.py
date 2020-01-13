# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
eval函数在Python中做数据类型的转换还是很有用的。它的作用就是把数据还原成它本身或者是能够转化成的数据类型。
那么eval和ast.literal_val()的区别是什么呢？
eval在做计算前并不知道需要转化的内容是不是合法的（安全的）python数据类型。只是在调用函数的时候去计算。如果被计算的内容不是合法的python类型就会抛出异常。
ast.literal则会判断需要计算的内容计算后是不是合法的python类型，如果是则进行运算，否则就不进行运算。
因此，推荐使用ast.literal_eval
JSON 的标准：双引号而非单引号！
这个问题是由于使用json.loads报错写的，这个时候可尝试ast.literal_eval
"""



import json
a = '{"test":"t"}'
b = "{'test':'t'}"
print(json.loads(a))
# print(json.loads(b)) # 这个地方用json.loads会报错
import ast

print(ast.literal_eval(b))


# 使用这个会获取当前目录文件(安全性问题)
eval("__import__('os').system('dir')")
# ast.literal_eval("__import__('os').system('dir')")  # 这句话就不会显示系统的文件，解决了安全性问题

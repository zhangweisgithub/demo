# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 都可以将str转换为对象
import json


a = "[null, true, false, 1]"         # 大写的True和False代表的是对象，小写的代表的是json      # [None, True, False, 1]
print(json.loads(a))
# print(eval(a))    # NameError: name 'null' is not defined

print(eval('1 + 1'))  # eval可以执行一个字符串表达式，并返回表达式的值
# json.loads('1+1')   会报错


b = "{'test':'set'}"
print(eval(b))
# print(json.loads(b))          # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes

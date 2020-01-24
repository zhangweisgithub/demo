# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json  # 导入python 中的json模块

l = ['iplaypython', [1, 2, 3], {'name': 'xiaoming'}]  # 创建一个l列表
encoded_json = json.dumps(l)  # 将l列表，进行json格式化编码
print(repr(l))        # Python repr() 函数将对象转化为供解释器读取的形式。
print(encoded_json)  # 输出结果(字符串)
print(type(encoded_json))  # json格式的字符串(如果对象中有单引号,应该可以考虑先dumps().loads())

print("-------------1---------------")

decode_json = json.loads(encoded_json)
print(type(decode_json))  # 查看一下解码后的对象类型
print(decode_json)  # 输出结果

print("-------------2---------------")

"""
json.dump和json.dumps很不同，json.dump主要用来json文件读写，和json.load函数配合使用。
json.dump(x,f)，x是对象，f是一个文件对象，这个方法可以将json字符串写入到文本文件中。
"""
data = {"a": "aaa", "b": "bbb", "c": [1, 2, 3, (4, 5, 6)]}
data2 = json.dumps(data)
print(data2)
f = open('./tt.txt', 'a')
json.dump(data2, f)

print("-------------3---------------")

f = open('./tt.txt', "r")
hehe = json.load(f)
print(hehe)

"""
json.dumps : dict转成str json.dump是将python数据保存成json
json.loads:str转成dict json.load是读取json数据 
"""

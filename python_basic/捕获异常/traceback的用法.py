# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""使用traceback获取详细的异常信息"""

# try:
#     1/0
# except Exception as e:
#     print (e)
# # integer division or modulo by zero :只知道是报了这个错,却不知道在哪个文件哪个函数的哪一行报错

import traceback

try:
    1 / 0
except Exception as e:
    # traceback.print_exc()          # 这个数据会直接打印在哪一行出现了什么类型的错误
    # print(traceback.format_exc())
    # traceback.format_exc():这个不会打印在控制台中,但是会返回一个字符串,除了不直接打印出来,效果跟traceback.print_exc()是一样的
    a = traceback.format_exc()
    print('as:', a)
error = "这是一个错误:" + "\n" + traceback.format_exc()  # 所以这个地方对错误的结果进行字符串拼接,就相当于个性化定制错误打印的日志格式
print(error)

"""
traceback.print_exc()与trackback.format_exc()区别:
trackback.format_exc()返回一个字符串,traceback.print_exc()回至二级打印出来,但是内容都是一样的
print_exc()还可以接受file参数直接写入到一个文件
"""

try:
    1 / 0
except Exception as e:
    traceback.print_exc(file=open("log.log", "a+", encoding="utf-8"))   # 注意文件打开添加utf-8,否者文件打不开
    # 这里可以接受一个file参数,将错误的信息打印到对应的文件中,这里如果是w+那么,每次有新的错误的话,会重置log.txt文件中的内容

"""
r:read
w:write    # w的情况下，只能write不能read，w+的情况下可以write 可以read
a:append
r+:read/update
w+:write/update
a+:append/update
"""

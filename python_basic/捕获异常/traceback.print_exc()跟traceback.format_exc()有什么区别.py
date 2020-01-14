# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
traceback可以定位到具体的哪一行出现了错误
traceback.print_exc可以把错误打印到指定的文件中
"""
import traceback


def test():
    try:
        a = 1 / 0
    except:
        # return traceback.print_exc(file=open("./test.log", "w+"))
        return traceback.print_exc()
        # format_exc()返回字符串，print_exc()则直接给打印出来。 即traceback.print_exc()与print traceback.format_exc()效果是一样的
        # return traceback.format_exc()


b = test()
print(b)

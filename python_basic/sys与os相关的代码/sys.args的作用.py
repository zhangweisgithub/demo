# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，关键就是要明白这参数是从程序外部输入的，
而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数。"""
import sys
a = sys.argv[1]              # python server.py dev
print(a)                     # a 的值就是dev,argv[0]打印的是文件名本身
b = sys.argv[2:]             # python sys.args的作用.py a b c d
print(b)                     # ['b', 'c', 'd']





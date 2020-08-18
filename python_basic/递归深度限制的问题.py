# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RecursionError: maximum recursion depth exceeded while calling a Python object
递归错误           最大的    递归深度         超过            调用
当调用该对象超过最大递归深度

"""
import sys


def func(depth):
    depth += 1
    print(depth)
    func(depth)


if __name__ == '__main__':
    print("最大递归深度:", sys.getrecursionlimit())
    sys.setrecursionlimit(2000)      # 默认的最大递归深度为1000,也可以进行设置最大递归深度为2000
    func(0)

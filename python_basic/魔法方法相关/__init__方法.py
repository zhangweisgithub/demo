# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__init__()基本使用:在方法中定义属性并设置初始值
__init__()方法叫做 对象的初始化方法，在 创建一个对象后默认会被调用，不需要手动调用
开发者可以 实现这个方法，并在该方法中定义属性并设置初始值
"""


class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth


b = Box(10, 20, 30)
print(b.getVolume())

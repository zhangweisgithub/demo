# !/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import random


def getRandomColor():
    """获取一个随机颜色(r,g,b)格式的"""
    c1 = random.randint(0, 256)
    c2 = random.randint(0, 256)
    c3 = random.randint(0, 256)
    return (c1, c2, c3)


# 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
image = Image.new("RGB", (150, 30), getRandomColor())
# 保存到硬盘，名为test2.png格式为png的图片
image.save(open("./photos/test2.png", "wb"), "png")

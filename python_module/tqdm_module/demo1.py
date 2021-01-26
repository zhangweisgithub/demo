# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加一个进度提示信息，用户只需要封装任意的迭代器 tqdm(iterator)。
总之，它是用来显示进度条的，很漂亮，使用很直观（在循环体里边加个tqdm），而且基本不影响原程序效率。
"""
import sys
import time
from tqdm import tqdm
from tqdm._tqdm import trange

for i in tqdm(range(100)):
    time.sleep(0.01)


print("hello world")

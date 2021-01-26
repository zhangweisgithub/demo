# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
将tqdm安装在这个文件的指定文件夹中 pip3 install --target
"""
import sys
import time
from tqdm import tqdm
from tqdm._tqdm import trange

for i in tqdm(range(100)):
    time.sleep(0.01)


print("hello world")

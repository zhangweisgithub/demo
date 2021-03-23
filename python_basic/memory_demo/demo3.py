# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
两个一起用，内存+硬盘缓存
二级缓存 双重缓存
"""
import time
import random
from functools import lru_cache
from joblib import Memory

memory = Memory(location="./cachedir")


@lru_cache(maxsize=5)
@memory.cache
def sum2(arg):
    time.sleep(1)
    list1 = [0, 1, 2]
    a = random.choice(list1)
    arg = 1 / a
    return arg


if __name__ == "__main__":
    while True:
        for i in ["a1", "b2", "e3", 'd4', 'e5']:
            arg = i
            t0 = time.time()
            try:
                res = sum2(arg)
                print("+++++++++++++++++++++++++++++++++++")
                print(i, res, "sum2 cost", time.time() - t0)
                print("+++++++++++++++++++++++++++++++++++")
            except:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        input_str = input("继续 or 结束")
        if input_str == 'q':
            break

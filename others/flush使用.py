# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python的stdout是有缓冲区的，给你个例子你就知道了
这个程序本意是每隔一秒输出一个数字，但是如果把这句话sys.stdout.flush()注释的话，你就只能等到程序执行完毕，屏幕上会一次性输出0，1，2，3，4。
如果你加上sys.stdout.flush()，刷新stdout，这样就能每隔一秒输出一个数字了。
可以用在网络程序中多线程程序，多个线程后台运行，同时要能在屏幕上实时看到输出信息。

以下代码的执行需要通过命令行执行才会生效
"""
import time
import sys

for i in range(5):
    print(i, end="")  # 这里要加一个end="", 意思是打印的时候不换行,将数据打印在一行才会有效果
    sys.stdout.flush()  # 如果有这一行,会看到01234依次打印,如果没有,一块打印
    time.sleep(1)

for i in range(5):
    print(i, end="", flush=False)      # print默认flush是False, 改成True就好了
    time.sleep(1)

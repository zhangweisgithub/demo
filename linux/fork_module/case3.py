# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fork()开启进程，主进程执行结束后，不会等待子进程:　
https://www.cnblogs.com/Magic-Dev/p/11405448.html
"""

# -*-coding:utf-8-*-
import os
import time

print('before calling')

p = os.fork()  # 主进程，子进程同时向下执行

print('after calling')

if p == 0:
    print('执行子进程, pid={} ppid={} p={}'.format(os.getpid(), os.getppid(), p))
    time.sleep(1)
    print('执行子进程, pid={} ppid={} p={}'.format(os.getpid(), os.getppid(), p))
else:
    print('执行主进程, pid={} ppid={} p={}'.format(os.getpid(), os.getppid(), p))

"""
[root@192 ~]# python case3.py 
before calling
after calling
执行主进程, pid=1648 ppid=1572 p=1649
after calling
执行子进程, pid=1649 ppid=1648 p=0
[root@192 ~]# 执行子进程, pid=1649 ppid=1 p=0             ----- 这个地方的ppid为什么是1?
"""

"""
现象:五秒前，两个进程都在执行，五秒后，主进程结束，只剩一个子进程(说明父进程没有等待子进程)，十秒后，子进程结束
结论:父进程执行结束后不等待子进程
问1的解释:子进程第一次打印时，刚好父进程还未结束，还可以获取到父进程ppid，因此第一次打印的ppid是父进程的pid，当睡了一秒以后，
父进程早就执行完了，溜了，没有等待子进程，因此子进程交给了init进程, ppid就变成1.
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
os.fork()这个函数，对于父进程，返回的是子进程的pid，对于子进程，返回的是0.
而通过os.getpid()得到的是当前的pid，os.getppid()得到的是父进程的pid.
"""
# multiprocessing.py
import os

print('Process (%s) start...' % os.getpid())
fork_num = 0
while fork_num < 3:
    pid = os.fork()
    fork_num += 1
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


"""
在运行之前，我们分析可以得到，经过三次循环，应该有8个进程 2^3=8
该函数在运行时，是将代码在子进程中复制了一份
"""

"""
Process (30121) start...
I (30121) just created a child process (30168).
I am child process (30168) and my parent is 30121.
I (30121) just created a child process (30169).
I am child process (30169) and my parent is 30121.
I (30121) just created a child process (30170).
I (30168) just created a child process (30171).
I am child process (30170) and my parent is 30121.
I am child process (30171) and my parent is 30168.
I (30169) just created a child process (30172).
I (30168) just created a child process (30173).
I am child process (30172) and my parent is 30169.
I am child process (30173) and my parent is 30168.
I (30171) just created a child process (30174).
I am child process (30174) and my parent is 30171.
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
首先，在python中我们要实现多进程，有两个模块可以用：
1）os中的fork()函数
2）multiprocessing模块
那么这两个模块有什么区别呢？
在fork()是基于unix/linux内核的函数，在windows中无法使用，因此multiprocessing模块作为跨平台的存在。
https://www.cnblogs.com/Magic-Dev/p/11405448.html
"""
# multiprocessing.py
import os

print('Process (%s) start...' % os.getpid())
print('before calling')
pid = os.fork()
print('after calling')
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

"""
Process (18738) start...
before calling
after calling
I (18738) just created a child process (18910).
after calling
I am child process (18910) and my parent is 18738.          # 这一行是子进行执行的结果
"""

"""
程序每次执行时，操作系统都会创建一个新进程来运行程序指令。进程中可调用os.fork,要求操作系统新建一个子进程.
每个进程都有一个不重复的进程ID号。或称pid，它对进程进行标识。子进程与父进程完全相同，子进程从父进程继承了多个值的拷贝。如全局变量和环境变量。
fork后，子进程接收返回值0，而父进程接收子进程的pid作为返回值

结论:调用os.fork()之后，主进程和子进程同时执行该行以下的代码，子进程中fork函数返回0，父进程中返回1630，即子进程的pid.
"""

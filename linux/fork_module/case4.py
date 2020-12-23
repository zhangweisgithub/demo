# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
僵尸进程:
子进程变成僵尸进程，是因为父进程先执行完，没有替子进程收尸。而wait()并不是用来收尸的，只是防止父进程先于子进程退出；如果父进程先退出，
会使子进程成为僵尸进程，这时候子进程的收尸就由1号init进程来回收。

"""

# -*-coding:utf-8-*-

import os
import time

p = os.fork()

if p == 0:
    time.sleep(10)
    print('执行子进程, pid={} ppid={} p={}'.format(os.getpid(), os.getppid(), p))
else:
    time.sleep(5)
    print('执行主进程, pid={} ppid={} p={}'.format(os.getpid(), os.getppid(), p))
    os.wait()

"""
现象:五秒前，两个进程都在执行，五秒后，主进程执行完成并调用了os.wait()，等待子进程结束，十秒后，子进程结束，父进程也随之结束
结论:父进程可调用os.wait()等待子进程结束。　　*没有子进程就调用os.wait()会抛异常:　OSError: [Errno 10] No child processes
"""

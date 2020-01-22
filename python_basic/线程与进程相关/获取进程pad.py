# !/usr/bin/env python
# -*- coding: utf-8 -*-
# getpid是获得当前进程的进程号。系统每开辟一个新进程就会为他分配一个进程号。在多进程的时候会用到
# 获得进程ID，之后可以操作这个进程，比如结束这个进程
# import os
# pid = os.fork()
# if pid == 0:
#     print("A", os.getpid(), os.getppid())
# else:
#     print("B", os.getpid(), os.getppid())


# a = ["ad"]
# b = [i for i in [{"key":"value"}]]
# for key in b:
#     a.append(key)
# print(b)
# print(a)


from multiprocessing import Process
import time
import random
import os


def task():
    print('%s is running' % os.getpid())
    time.sleep(random.randrange(1, 3))
    print('%s is end' % os.getpid())


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()  # 等待p停止,才执行下一行代码
    print('主进程!')

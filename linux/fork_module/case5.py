# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
进程间资源独立:
https://www.cnblogs.com/Magic-Dev/p/11405448.html
"""
# -*-coding:utf-8-*-

import os
import time

variable = []
p = os.fork()
if p == 0:
    variable.append(1)
    print('子进程 variable_id={}'.format(id(variable)))
    print('子进程 variable={}'.format(variable))
else:
    time.sleep(1)  # 睡一秒，让子进程先改变变量的值
    print('主进程 variable_id={}'.format(id(variable)))
    print('主进程 variable={}'.format(variable))
    os.wait()
"""
[root@192 ~]# python fork.py 
子进程 variable_id=140426199897224
子进程 variable=[1]
主进程 variable_id=140426199897224
主进程 variable=[]
"""


"""
结论:子进程中改变了变量的值，但在父进程中并未改变，说明进程间全局变量不共享
问2:但为什么变量id一样?
问2的解释:  写时复制技术：内核只为新生成的子进程创建虚拟空间结构，它们复制于父进程的虚拟空间结构，但是不为这些段分配物理内存，
它们共享父进程的物理空间，当父子进程中有更改相应段的行为发生时，再为子进程相应的段分配物理空间。
因此不论子进程有没有修改操作，虚拟地址和父进程是一样的，两个进程查看变量的id值是相同的。
 另外，即使是两个互不相干的进程，若它们的逻辑地址相同，实际地址也是不同的，并不会产生冲突。
"""

# -*- coding: utf-8 -*-
# @Time    : 2018-04-28 21:31
# @Email   : Yzh_smlie@163.com
# @File    : Q进程间通信.py

import time
from multiprocessing import Process, Queue

q = Queue()  # 创建列队，不传数字表示列队不限数量
for i in range(11):
    q.put(i)


def A():
    while 1:
        try:
            num = q.get_nowait()
            print('我是进程A,取出数字:%d' % num)
            time.sleep(1)
        except:
            break


def B():
    while 1:
        try:
            num = q.get_nowait()
            print('我是进程B,取出数字:%d' % num)
            time.sleep(1)
        except:
            break


p1 = Process(target=A)
p2 = Process(target=B)
p1.start()
p2.start()

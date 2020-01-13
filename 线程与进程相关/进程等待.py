# !/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from time与datetime import time


def func(args):
    time.sleep(1)   # 休眠1s
    print("%s------>%s" % (args, time.ctime()))    # 打印传递的参数及时间


if __name__=="__main__":
    p1 = Pool(2)  # 定义2个进程池(子进程必须从进程池中取出空闲的进程)
    for i in range(10): # 定义循环10次
        p1.apply_async(func=func,args=(i,)) # 异步执行任务

    p1.close()      # 等待所有的任务都完成才关闭进程池
    p1.join()
    print("ending")
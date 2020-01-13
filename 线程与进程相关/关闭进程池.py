# !/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from time与datetime import time


def func(args):
    time.sleep(1)   #程序休眠1s
    print("%s------>%s" % (args, time.ctime()))    #打印参数及时间


if __name__=="__main__":
    p1=Pool(2)  #设定开启2个进程池
    for i in range(10):
        p1.apply_async(func=func,args=(i,)) #设定异步执行任务

    p1.close()  #关闭进程池
    time.sleep(2)   #程序休眠2s
    p1.terminate()  #关闭进程池
    p1.join()   #阻塞进程池
    print("ending")     #打印结束语句
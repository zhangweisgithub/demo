# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool


def func1(a):
    print("开始func1:%s" % a)
    time.sleep(3)
    print("结束func1:%s" % a)


def func2(b):
    print("开始func1:%s" % b)
    time.sleep(20)
    print("结束func1:%s" % b)


if __name__ == '__main__':
    print("开始执行主进程")
    start_time = time.time()
    # 使用进程池创建子进程
    pool = Pool(2)
    print("开始执行子进程")
    pool.apply_async(func1, ("test1",))
    pool.apply_async(func2, ("test2",))
    pool.close()
    pool.join()
    # 进程池调用close方法后，会把进程池状态改为不可再插入元素的状态，但并未关闭进程池
    # close必须在join之前调用。
    # join()调用后主进程必须等子进程全部运行结束后才接着运行主进程。
    print("主进程结束耗时%s" % (time.time() - start_time))


# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""apply_async 是异步非阻塞的。即不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。
首先主进程开始运行，碰到子进程后，主进程仍可以先运行，等到操作系统进行进程切换的时候，
在交给子进程运行。可以做到不等待子进程执行完毕，主进程就已经执行完毕，并退出程序"""
import time
from multiprocessing import Pool


def run(count):
    print('子进程编号:%s' % count)
    time.sleep(2)
    print('子进程%s结束' % count)


if __name__ == "__main__":
    print("开始执行主程序")
    start_time = time.time()         # time.time()记录的为时间戳,可以计算两个时间差
    print("start_time:", start_time)
    # 使用进程池创建子进程
    pool = Pool(4)
    print("开始执行子进程")
    for i in range(4):
        pool.apply_async(run, (i,))
    print("主进程结束耗时%s" % (time.time() - start_time))


"""
开始执行主程序
开始执行子进程
主进程结束耗时0.131000041962
"""



"""
进程的切换是操作系统来控制的，是抢占式的切换。 我们首先运行的是主进程，由于主进程代码很简单，主进程一下子就运行完毕了，所以子进程完全没有机会切换到程序就已经结束了。

如果我们想要子进程执行完毕后再运行主进程剩余部分，则在恰当位置上加上一句子进程名.join()。这样就告诉主进程等该子进程执行完毕后，再运行主进程剩余部分
"""
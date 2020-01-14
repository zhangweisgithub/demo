# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool

"""
官方建议放弃:apply,尽量使用apply_async

apply是阻塞的。首先主进程开始运行，碰到子进程，操作系统切换到子进程，等待子进程运行结束后，
在切换到另外一个子进程，直到所有子进程运行完毕。然后在切换到主进程，运行剩余的部分。这样跟单进程串行执行没什么区别
子进程是顺序执行的，且子进程全部执行完毕后才继续执行主进程
"""


def run(count):
    print("子进程编号:%s" % count)
    # time.sleep(1)
    print("子进%s程结束" % count)


if __name__ == '__main__':
    print("开始执行主进程")
    start_time = time.time()           # 这个地方显示的为时间戳
    print("start_time:", start_time)
    pool = Pool(4)          # 使用进程池创建子进程
    print("开始执行子进程")
    for i in range(4):
        print(i)
        pool.apply(run, args=(i, ))
    print("主进程结束,总耗时:%s" % (time.time() - start_time))


# 得到如下执行结果
"""
开始执行主进程
('start_time:', 1548923234.95)
开始执行子进程
子进程编号:0
子进0程结束
子进程编号:1
子进1程结束
子进程编号:2
子进2程结束
子进程编号:3
子进3程结束
主进程结束,总耗时:8.23000001907
"""

















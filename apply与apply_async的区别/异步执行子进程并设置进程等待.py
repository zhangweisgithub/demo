# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
如果我们想要子进程执行完毕后再运行主进程剩余部分，则在恰当位置上加上一句子进程名.join()。
这样就告诉主进程等该子进程执行完毕后，再运行主进程剩余部分,close必须在join前调用
python官方建议：废弃apply，尽量使用apply_async。
"""
import time
from multiprocessing import Pool


def run(count):
    print('子进程编号:%s' % count)
    time.sleep(2)
    print('子进程%s结束' % count)


if __name__ == "__main__":
    print("开始执行主程序")
    start_time = time.time()
    # 使用进程池创建子进程
    pool = Pool(4)
    print("开始执行子进程")
    for i in range(4):
        pool.apply_async(run, args=(i,))
    pool.close()
    pool.join()
    # 进程池调用close方法后，会把进程池状态改为不可再插入元素的状态，但并未关闭进程池
    # close必须在join之前调用。
    # join()调用后主进程必须等子进程全部运行结束后才接着运行主进程。
    print("主进程结束耗时%s" % (time.time() - start_time))

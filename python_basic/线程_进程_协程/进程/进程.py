# !/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import os
import time
import signal


def sing():
    print(multiprocessing.current_process(), "获取当前的子进程")     # 获取当前的子进程
    # 结果  <Process(Process-1, started)> 获取当前的子进程
    print(multiprocessing.current_process().pid, "当前进程的进程编号")   # 14032 当前进程的进程编号
    # 获取当前进程编号和父进程编号
    print(os.getpid(), os.getppid())     # 结果:14032 13496
    for i in range(5):
        print("唱歌...", i + 1)
        time.sleep(0.1)
        # os.kill(os.getpid(), signal.SIGKILL)


def dance():
    for i in range(5):
        print("跳舞......", i+1)
        time.sleep(0.1)


if __name__ == '__main__':
    print(multiprocessing.current_process())         # 结果:<_MainProcess(MainProcess, started)>
    print(multiprocessing.active_children())         # 结果:[]
    print(os.getpid(), "我是main进程")               # 结果:13496 我是main进程
    # 创建多进程实现多任务
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    p2.start()
    # 开启两个子进程之后会有两个活动的子进程
    print(multiprocessing.active_children())  # 结果:<Process(Process-1, started)>, <Process(Process-2, started)>
    print("主进程执行完毕")

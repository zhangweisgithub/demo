# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 需求:在同一时间完成多个任务
# 办法:多线程!
import threading   # 导入多线程
import time


def sing():
    for i in range(5):
        print("唱歌...", i + 1)
        # 添加延时操作,能够看到多任务同时进行
        time.sleep(0.1)


def dance():
    for i in range(5):
        print("跳舞......", i + 1)
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建两个线程,分别执行唱歌和跳舞
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
# 守护线程 :主线程走完了,子线程无论走到哪里,结束!!!
# 设置子线程守护主线程:要在子线程开始之前
# t1.setDaemon(True)
# t2.setDaemon(True)
    t1.start()     # 启动线程,即让线程开始执行
    t2.start()
# 等待线程 :子线程走完,主线程才开始
# t1.join()
# t2.join()
    print("主程序执行完毕")    # 主程序的执行与线程部分先后

# 主线程默认会执行完毕,然后等待子线程全部执行完毕以后再停止主线程

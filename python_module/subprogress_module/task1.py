# !/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time

def task_handler():
    # handle task here
    time.sleep(5)
    print("task1")


def start_a_process_for_task():
    print("开始执行multiprocessing......")
    p = multiprocessing.Process(target=task_handler, args=())
    p.start()
    return 0


if __name__ == '__main__':
    ret = start_a_process_for_task()
    print("ret:", ret)

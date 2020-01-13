# -*- coding: utf-8 -*-
# @Time    : 2018-05-03 16:04
# @Email   : Yzh_smlie@163.com
# @File    : 多进程.py


from multiprocessing import Process
import time


def run_proc():
    """⼦进程要执⾏的代码"""
    while True:
        print("----2----")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while True:
        print("----1----")
        time.sleep(1)

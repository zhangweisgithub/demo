# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from threading import Timer, Thread


# def func():
#     print('执行我啦')
#
#
# Timer(5, func).start()          # 设置5s钟之后执行函数
# print('主线程')

def test1():
    def test(a):
        print("执行线程!")
        time.sleep(2)
        print(a)

    print("执行主函数")
    th = Thread(target=test, args=("test", ))
    th.start()
    print("主函数结束")


test1()

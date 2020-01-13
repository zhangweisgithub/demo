# !/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time


def test():
    f = open("test.txt","a")
    f.write("test_write" + "\n")
    time.sleep(1)
    mutex.acquire()      # 取得锁
    f.close()
    mutex.release()      # 释放锁


if __name__ == '__main__':
    mutex = threading.Lock()    # 创建锁
    for i in range(5):
        t = threading.Thread(target=test)
        t.start()

"""
不加锁的结果:
test_write
test_write

 线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。互斥锁为资源引入一个状态：锁定/非锁定。
 某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，
 其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

加了线程锁之后的结果:
test_write
test_write
test_write
test_write
test_write
"""









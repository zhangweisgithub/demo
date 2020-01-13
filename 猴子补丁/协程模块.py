# !/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent

"""如下可以看到执行顺序是来回切换的,gevent.sleep()不会阻塞整个线程
如果换成time.sleep(),那么会先执行完foo(),再执行bar,线程就变成阻塞的了
"""
import time

def foo():
    print('Running in foo')
    gevent.sleep(0)  # 这行的作用是什么？   gevent.sleep会释放cpu控制权，即切换协程，从而不阻塞其他协程运行
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)  #
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])

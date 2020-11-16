# !/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import threading
import time
import traceback


class MyThread(threading.Thread):
    """
        某个类没有我要的方法，那么可以重写这个类，添加我需要的方法
    """

    def __init__(self, target=None, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.args = args
        self.result = None

    def run(self):
        try:
            self.result = self.func(*self.args)
        except Exception:
            print(traceback.print_exc())

    def get_result(self):
        return self.result


def tstart(arg, name):
    for i in range(1, arg):
        print(name + ' sleep ' + str(i) + ' second\n')
        time.sleep(i)
    return "%s running end" % name


if __name__ == '__main__':
    task_list = []
    t1 = MyThread(tstart, args=(5, 'thread 1'))
    task_list.append(t1)
    t1.start()

    t2 = MyThread(tstart, args=(6, 'thread 2'))
    task_list.append(t2)
    t2.start()

    for t in task_list:
        t.join()

    while len(task_list) != 0:
        for t in task_list:
            if not t.isAlive():
                result = t.get_result()
                if result:
                    print("获取到了结果:", t.get_result())
                else:
                    print('create server error')
                task_list.remove(t)

    print("main func end")

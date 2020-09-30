# !/usr/bin/env python
# -*- coding: utf-8 -*-


import multiprocessing
import threading
from time import sleep

from jsonpath import xrange


def task_processor():
    sleep(10)


class TaskProxy(threading.Thread):
    def __init__(self):
        super(TaskProxy, self).__init__()

    def run(self):
        p = multiprocessing.Process(target=task_processor, args=())
        p.start()
        p.join()


def task_handler():
    t = TaskProxy()
    t.daemon = True
    t.start()
    return


for _ in xrange(0, 20):
    task_handler()

sleep(60)


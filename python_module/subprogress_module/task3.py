# !/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

import os
import signal
import time
from multiprocessing import Process


def child_exited(sig, frame):
    pid, exitcode = os.wait()
    print("Child process {pid} exited with code {exitcode}".format(
        pid=pid, exitcode=exitcode
    ))


def worker():
    time.sleep(5)
    print("Process {pid} has completed it's work".format(pid=os.getpid()))


def parent():
    children = []

    # Comment out the following line to see zombie children
    signal.signal(signal.SIGCHLD, child_exited)

    for i in range(5):
        c = Process(target=worker)
        c.start()
        print("Parent forked out worker process {pid}".format(pid=c.pid))
        children.append(c)
        time.sleep(1)

    print("Forked out {c} workers, hit Ctrl+C to end...".format(c=len(children)))
    while True:
        time.sleep(5)


if __name__ == '__main__':
    parent()

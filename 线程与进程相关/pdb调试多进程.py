# !/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import pdb


def child_process():
    print("Child-Process")
    pdb.Pdb(stdin=open('test.txt', 'r+'), stdout=open('test.txt', 'w+')).set_trace()
    var = "debug me!"
    print(var)


def main_process():
    print("Parent-Process")
    p = multiprocessing.Process(target=child_process)
    p.start()
    pdb.set_trace()
    var = "debug me!"
    p.join()
    print(var)


if __name__ == "__main__":
    main_process()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from line_profiler import LineProfiler

"""
分析时间耗时,
这个包需要下载到本地进行安装:
pip3 install ./python_module/memory_profiler_module/line_profiler-3.1.0-cp37-cp37m-win_amd64.whl
"""


def operation1():
    num = 0
    for i in range(10000):
        num += 1


def operation2():
    num = 0
    while (num < 10000):
        num += 1


if __name__ == "__main__":
    lprofiler = LineProfiler(operation1, operation2)
    lprofiler.run('operation1()')
    lprofiler.run('operation2()')
    lprofiler.print_stats()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pysnooper
"""可以将日志文件进行重定向"""


@pysnooper.snoop("./pysnooper.log")
# @pysnooper.snoop()       # 没有指定日志的话就执行打印在了控制台
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


number_to_bits(6)



















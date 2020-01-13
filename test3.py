# !/usr/bin/env python
# -*- coding: utf-8 -*-
import dis
def swap1():
    x, y = 2, 3
    x, y = y, x

def swap2():
    x, y = 2, 3
    temp = x
    x = y
    y = temp

dis.dis(swap1)
dis.dis(swap2)
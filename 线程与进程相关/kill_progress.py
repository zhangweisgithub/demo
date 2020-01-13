# !/usr/bin/env python
# -*- coding: utf-8 -*-
from time与datetime import datetime, time

# def test():
#     print("1")
#     time.sleep(60*5)
#     print("2")

st = datetime.datetime.now()
print(st)
time.sleep(4)
et = datetime.datetime.now()
ta = (et - st).seconds
print(ta)

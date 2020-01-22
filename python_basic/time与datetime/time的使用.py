# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time

res = time.time()  # 1579677598.4181433
print(f"获取时间戳:{res}")
time.sleep(0.5)
res2 = time.time()
print("时间差:", res2-res)


print("-----------------------------------------")
res = time.localtime()  # 用是格式化时间戳为本地的时间
print(res)
# time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=15, tm_min=21, tm_sec=34, tm_wday=2, tm_yday=22, tm_isdst=0)


res = time.gmtime()  # 同上
print(res)

var = time.mktime(res)  # mktime() 结构化时间转换为时间戳
print(var)  # 1579649080.0

print("-----------------------------------------")
res = time.ctime()  # Wed Jan 22 15:26:18 2020
print(res)

res = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 2020-01-22 15:26:50
print(res)

var = time.strptime(res, "%Y-%m-%d %X")
# time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=15, tm_min=27, tm_sec=13, tm_wday=2, tm_yday=22, tm_isdst=-1)
print(var)
print(type(var))  # <class 'time.struct_time'>

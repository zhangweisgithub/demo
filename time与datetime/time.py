# !/usr/bin/env python
# -*- coding: utf-8 -*-
from time与datetime import datetime
import time
"""
1.days：来获取时间差的天数
2.seconds：来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数
3.total_seconds：来获取准确的时间差，并将时间差转换为秒"""

date = datetime.datetime.strptime("2014-09-25", "%Y-%m-%d")
print(date)
print(type(date))


# start = datetime.datetime.now()
# fort_start = time.strftime("%Y-%m-%d %H:%M:%S", start)
# print(fort_start)
#
# import time
# time.sleep(2.2)
# end = datetime.datetime.now()
# fort_end = time.strftime("%Y-%m-%d %H:%M:%S", end)
# print(fort_end)
# run_time = (end-start).total_seconds()/3600
# print(run_time)
#
# # 运行时间
# print("运行时间:%.4f"%run_time)

# start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(start)
start_time = datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '%Y-%m-%d %H:%M:%S')
print(start_time)
time.sleep(4.2)
# end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
end_time = datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '%Y-%m-%d %H:%M:%S')
print(end_time)
total_time = (end_time - start_time)
print("用时总长:%s"%total_time)


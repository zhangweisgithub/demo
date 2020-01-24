# -*- coding: utf-8 -*-
# @Time    : 2018-04-27 14:36
# @Email   : Yzh_smlie@163.com
# @File    : 03-.py


import time
import datetime

# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
print(threeDayAgo)
# 转换为时间戳:
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
print(timeStamp)
# 转换为其他字符串格式:
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")

print(otherStyleTime)

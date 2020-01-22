# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""datetime在设置update_time的时候,需在把onupdate=datetime.now生成一个时间对象,使时间在创建的时候生成(动态时间)"""
from datetime import datetime

a = datetime.now()  # "当前时间:2018-12-28 14:56:11.452010
b = datetime.now  # <built-in method now of type object at 0x921b20>
print(a)
print(b)

print(f"世界标准时间:{datetime.utcnow()}")  # "世界标准时间:"2018-12-28 07:26:08.817000
print(datetime(2018, 12, 15, 12, 30, 10))  # 输出指定时间:2018-12-15 12:30:10

print("-------------------我是分割线----------------------")

print(datetime.now().strftime("%m/%d/%Y %H:%S:%M"))  # strftime 将时间按照指定格式输出, 得到的数据类型为一个字符串
print(datetime.strptime('2018/08/12', "%Y/%m/%d"))  # strptime将字符串转换为datatime类型的数据:2018-08-12 00:00:00
print(f"今天是今年的第{datetime.now().strftime('%j')}天")  # 今天是今年的第362天

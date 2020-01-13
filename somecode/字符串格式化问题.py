# -*- coding: utf-8 -*-
# @Time    : 2018-05-15 10:42
# @Email   : Yzh_smlie@163.com
# @File    : 字符串格式化问题.py

'''
format 和 %的区别


'''
# 定义一个坐标值
c = (250, 250)
# 使用%丑陋的格式化...
s1 = "敌人坐标：%s" % (c,)
print(s1)
# 而使用 format 就不会存在上面的问题：

# 定义一个坐标值
c = (250, 250)
# 使用format格式化
s2 = "敌人坐标：{}".format(c)
print(s2)
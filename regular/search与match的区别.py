# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
s = "小明年龄18岁, 工资10000"
res = re.search(r"\d+", s).group()
print("search匹配第一个匹配到的数据:", res)

res = re.findall(r"\d+", s)
print("findall的结果:满足正则都匹配", res)

res = re.match("小明", s).group()
print("匹配以小明开头的字符并匹配出小明", res)

# res = re.match("工资", s).group()
# print("match结果:工资不是字符串开头，匹配不到，报错！", res)

# res = re.match(r"\d+", s)
# print("不加group为none,匹配不到", res)




"""
match和search都是测试正则表达式与字符串是否匹配，不同的是，match要求字符串的第一个字符就能匹配上正则表达示，
而search则不同，如果字符串开头不能匹配，即会继续往后匹配，直接匹配成功或者到字符串结束。
"""





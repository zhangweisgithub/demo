# -*- coding: utf-8 -*-
# @Time    : 2018-05-13 18:04
# @Email   : Yzh_smlie@163.com
# @File    : 老师分教室.py

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配.
import random

# 定义一个列表来保存3个办公室
offices = [[], [], []]

# 定义一个列表来存储8位老师的名字
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 开始分配
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

# 遍历输出分配结果
i = 1
for tempNames in offices:
    print('办公室%d中有%d个老师，分别是：' % (i, len(tempNames))),
    i += 1
    for name in tempNames:
        print('%s' % name),
    print('\n')

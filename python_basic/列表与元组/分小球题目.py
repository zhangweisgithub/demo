# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现
"""
import random

balls = ["红", "红", "红", "蓝", "蓝", "蓝", "白", "白", "白", "白"]
boxes = [[], [], []]
for box in boxes:
    i = balls.index("白")
    box.append(balls.pop(i))
print(boxes)
for ball in balls:
    boxes[random.randint(0, 2)].append(ball)
print(boxes)

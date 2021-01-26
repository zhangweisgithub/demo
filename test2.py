# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
balls = ["红","红","红","蓝","蓝","蓝","白","白","白","白"]
boxes = [[],[],[]]
for box in boxes:
    i = balls.index("白")
    box.append(balls.pop(i))
print(boxes)
for ball in balls:
    boxes[random.randint(0,2)].append(ball)
print(boxes)
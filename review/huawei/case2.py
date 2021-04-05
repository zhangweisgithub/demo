# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/qq_42233538/article/details/108395443
1.计算偏移坐标围城的面积

     小明从原点（0,0）开始沿着X轴前进，e为终点，过程中遇到 x offset y 则向Y轴方向偏移y，计算由X轴、x=e和走的路径围成的面积；

输入：

第一行：n e （中间用空格间隔，n:输入的点的个数，e:终点位置）

接下来n行：x y  (x offset y 表示在坐标x处，向Y轴偏移y)

输出：

     围成的面积
输入:
4 10
1 1
2 1
3 1
4 -2

输出:
12
"""
n, e = list(map(int, input().split()))
w = []
arr_s = []
for i in range(n):
    w0 = list(map(int, input().split()))
    print(w0)
    print(len(w0))
    if len(w) == 0:
        w.append(w0)
    else:
        s = abs((w0[0] - w[-1][0]) * w[-1][1])
        arr_s.append(s)
        w.append([w0[0], w0[1] + w[-1][1]])
if w[-1][0] < e:
    s = abs((e - w[-1][0]) * w[-1][1])
    arr_s.append(s)
# print(w)
# print(arr_s)
print(sum(arr_s))


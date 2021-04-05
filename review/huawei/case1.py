# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
【算法】统计连续重复字符串的字母出现次数
输入:
AABAA
2

输出
1
"""
str1 = "aaagmbbbbaaaaafmm"  # 若a分别出现连续的两段，若后一段出现的字母次数多，则取较大值

dict1 = {}
i = 0

input = 100
temp_zifu = str1[0]

for m in range(1, len(str1)):
    if str1[m] != temp_zifu:
        cisu = m - i
        if temp_zifu not in dict1.keys():
            dict1[temp_zifu] = cisu
        else:
            dict1[temp_zifu] = max(dict1[temp_zifu], cisu)
        i = m  # i只有在遇到不同字符才向后移动
        temp_zifu = str1[m]

    if str1[m] == temp_zifu and m == len(str1) - 1:  # 处理最后相同字符的情况 aabbb
        cisu = m - i + 1
        if temp_zifu not in dict1.keys():
            dict1[temp_zifu] = cisu
        else:
            dict1[temp_zifu] = max(dict1[temp_zifu], cisu)

print(dict1)

a = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

b = [item[1] for item in a]
print(b)  # [5, 4, 2, 1, 1]

c = sorted(b, reverse=True)

print(c)
print(1)

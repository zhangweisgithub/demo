# -*- coding: utf-8 -*-
# @Time    : 2018-04-27 14:40
# @Email   : Yzh_smlie@163.com
# @File    : 04-.py

ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]

# 第一种  有序排列
# ids = list(set(ids))
# print(ids)


# 第二种  无序排列
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)

print(news_ids)
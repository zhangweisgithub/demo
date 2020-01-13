# !/usr/bin/env python
# -*- coding: utf-8 -*-

# a= [{1: u'Zhu Jiqing'}, {4: u'Xiao Liping'}, {5: u'Xiao Liping'}, {1: u'Wang Canbin'}, {2: u'Wang Canbin'}, {4: u'Wang Canbin'}, {5: u'Wang Canbin'}, {1: u'Zhang Chaohui'}, {2: u'Zhang Chaohui'}, {3: u'Zhang Chaohui'}]
#
# num = [{1:["name"]}]
# for i in a:
#     print(i.keys())
from collections import defaultdict
# list2 = [{"a": [123,456]},{"b": [789]}]
# # list2 = [{"a": 123},{"a": 456}, {"b": [789]}]
# dic = {}
# for i in list2:
#     for k,v in i.items():
#         dic.setdefault(k, []).append(v)
# print [{k:v} for k,v in dic.items()]
list1 = [{"a": 123}, {"a": 23}, {"b": 12}]
dic = {}
for i in list1:
    for k, v in i.items():
        dic.setdefault(k, []).append(v)
print(dic)
print [{k: v} for k, v in dic.items()]
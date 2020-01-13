# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json

dict = {"name": "zhangwei", "age": 18, "city": "深圳", "tel":"1234567889"}
# dict.items()结果是字典的键值对元组
list = sorted(dict.items(), key=lambda i: i[0], reverse=False)
print ("sorted根据字典键排序:",list)


new_dict = {}
for i in list:
    new_dict[i[0]] = i[1]
print (json.dumps(new_dict, encoding="utf-8", ensure_ascii=False))







# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 18:40
# @Email   : Yzh_smlie@163.com
# @File    : 字典的操作.py

# 字典推导式
# d = {key: value for (key, value) in iterable}

dic1 = {'name': 'zs', 'age': 13}
# 删除键值对
del dic1['name']
print(dic1)

# 合并字典键值对
dic2 = {'name': 'ls'}
dic1.update(dic2)
print(dic1)

# 根据键从小到大排序
dict1 = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
list = sorted(dict1.items(), key=lambda i: i[0], reverse=False)
print('sorted根据字典键排序', list)
new_dict = {}
for i in list:
    new_dict[i[0]] = i[1]
print('新字典', new_dict)

# 使用pop和del删除字典中的"name"字段，
dic = {"name": "zs", "age": 18}
dic.pop("name")
print(dic)

dic = {"name": "zs", "age": 18}
del dic['name']
print(dic)

'''
python字典和json字符串相互转化方法
json.dumps()字典转json字符串，
json.loads()json转字典
'''

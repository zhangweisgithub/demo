# !/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath

"""
测试jsonpath的使用
"""

json_str = {'code': 0, 'demands': [
    {'created_time': '2020-07-21 10:23:47', 'creator': 'zhangwei_vendor', 'demand_no': '', 'description': '',
     'id': 16693, 'modifier': 'ZhouQing', 'module': None, 'project_id': 179, 'project_name': '测试专用', 'title': '关联需求',
     'typo': None, 'updated_time': '2020-08-06 19:56:05', 'version_id': '19082,319', 'version_name': '3.3.1,3.3.2'},
    {'created_time': '2020-07-21 10:23:29', 'creator': 'zhangwei_vendor', 'demand_no': '', 'description': '',
     'id': 16692, 'modifier': 'zhangwei_vendor', 'module': None, 'project_id': 179, 'project_name': '测试专用',
     'title': '关联需求2', 'typo': None, 'updated_time': '2020-07-21 10:23:29', 'version_id': '19082,319',
     'version_name': '3.3.1,3.3.2'},
    {'created_time': '2020-07-21 10:23:06', 'creator': 'zhangwei_vendor', 'demand_no': '', 'description': '',
     'id': 16691, 'modifier': 'zhangwei_vendor', 'module': None, 'project_id': 179, 'project_name': '测试专用',
     'title': '关联需求1', 'typo': None, 'updated_time': '2020-07-21 10:23:06', 'version_id': '19082,319',
     'version_name': '3.3.1,3.3.2'}], 'total': 3, 'elapsed': 68.513, 'status_code': 200}
property_path = "demands.0.title?"
# property_path = "demands.-1:.title?"     # 如果是负索引,需要在负索引后面添加 :
property_path = property_path[:-1]  # 去除结尾的"?"
#
# property_path = "code"
temp_value = jsonpath.jsonpath(json_str, property_path)
print(temp_value)
# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""json.dumps()字典转化为json字符串,json.loads()将json转字典"""
import json
dic = {"name": "zhangwei", "age": 18}
res = json.dumps(dic)
print res, type(res)       # {"name": "zhangwei"} <type 'str'>

ret = json.loads(res)
print ret, type(ret)            # {u'name': u'zhangwei'} <type 'dict'>


"""
字典的格式是字典，json的格式是字符串，在传输的时候用的是字符串，所以如果要传输字典内容，就需要先进行字典转json。
json中必须使用双引号，dict则可以用单引号也可以用双引号
"""


"""
json.dump()/json.load()  和  json.dumps()/json.loads() 区别

json.dumps()/json.loads()用来编码和解码json字符串数据

json.dump()/json.load()用来处理文件

import json
json_content = {'a':'1111','b':'2222','c':'3333','d':'4444'}
with open('json_file.json','w') as f:
    json.dump(json_content, f)

with open('json_file.json', 'r') as f:
    content = json.load(f)
    print(content)

"""








# -*- coding: utf-8 -*-
import urllib2
import jsonpath
import json
import chardet

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()

# print(html)    # 这里得到的html是json格式的数据,然后我们需要把json格式字符串转换成python对象(也就是说转化为字典对象

jsonobj = json.loads(html)
citylist = jsonpath.jsonpath(jsonobj, '$..name')        # 从根节点开始，匹配name节点(得到的是一个列表,asc编码的列表)
print type(citylist)
# fp = open('city.json', 'w')

# dumps不仅可以把字典转化为json数据,实质上是python对象转化为我们想要的数据
content = json.dumps(citylist, ensure_ascii=False)
print content

# fp.write(content.encode('utf-8'))

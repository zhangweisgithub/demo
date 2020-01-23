# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
IOError：输入输出异常
AttributeError：试图访问一个对象没有的属性
ImportError：无法引入模块或包，基本是路径问题
IndentationError：语法错误，代码没有正确的对齐
IndexError：下标索引超出序列边界
KeyError:试图访问你字典里不存在的键
SyntaxError:Python代码逻辑语法出错，不能执行
NameError:使用一个还未赋予对象的变量
"""

"""
----常见的状态码
200 oK
请求正常处理完毕
204 No Content
请求成功处理，没有实体的主体返回
206 Partial Content
GET范围请求已成功处理
301 Moved Permanently
永久重定向，资源已永久分配新URI
302 Found
临时重定向，资源已临时分配新URI
303 See Other
临时重定向，期望使用GET定向获取
304 Not Modified
发送的附带条件请求未满足
307 Temporary Redirect
临时重定向，POST不会变成GET
400 Bad Request
请求报文语法错误或参数错误
401 Unauthorized
需要通过HTTP认证，或认证失败
403 Forbidden
请求资源被拒绝
404 Not Found
无法找到请求资源（服务器无理由拒绝）
500 Internal Server Error
服务器故障或Web应用故障
503 Service Unavailable
服务器超负载或停机维护
"""
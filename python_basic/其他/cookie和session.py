# -*- coding: utf-8 -*-
# @Time    : 2018-05-09 10:51
# @Email   : Yzh_smlie@163.com
# @File    : cookie和session.py

'''
1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，
    如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，
    值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差
'''
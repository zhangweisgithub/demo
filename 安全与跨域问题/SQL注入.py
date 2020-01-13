# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，比如例子中的SQL注入会删除数据库demo
"""
input_name = "sz"
sql = 'select * from demo where name="%s"' % input_name
print("正常的sql语句:",sql)

input_name = "sz; drop database demo"
sql = 'select * from demo where name="%s"' % input_name
print ("sql注入语句",sql)

# 解决方法:通过传参的方式解决sql注入
params = [input_name]
count = cs1.execute("select * from goods where name=%s", params)










# !/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

new_md5 = hashlib.md5()  # 创建hashlib的md5对象
new_md5.update('字符串'.encode())  # 将字符串载入到md5对象中，获得md5算法加密。
print(new_md5.hexdigest())  # 通过hexdigest()方法，获得new_md5对象的16进制md5显示。

"""
md5加密只能单向,不能反向逆推,但是可以通过先生成md5的库然后去撞数据库的方法进行破解
所以,现在需要考虑加盐的方式进行加密
"""

yan = '!任#意%字^符@'  # 定义加盐字符串
pwd = input(">>>")   # 这里输入需要加密的字符串

md5_pwd = hashlib.md5()
md5_pwd.update((pwd + yan).encode('UTF-8'))  # 加盐
pwd = md5_pwd.hexdigest()
print(pwd)
# pwd = hashlib.new('md5',(pwd+yan).encode('UTF-8')).hexdigest()   #也可以这样简写哦。。一句话搞定。

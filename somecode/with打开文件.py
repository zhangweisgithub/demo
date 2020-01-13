# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 19:00
# @Email   : Yzh_smlie@163.com
# @File    : with打开文件.py

# f = open("test.text", "wb")
# try:
#     f.write("hello word")
# except:
#     pass
# finally:
#     f.close()

'''
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open
写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，
都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close
'''
with open('test.text', "w") as f:
    f.write('hello')

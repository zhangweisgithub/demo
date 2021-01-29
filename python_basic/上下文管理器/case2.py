# !/usr/bin/env python
# -*- coding: utf-8 -*-
class MyManager:
    def __enter__(self):
        print('连接资源')
        return '我是 __enter__() 方法的返回值'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出连接')

    def show(self):
        print('资源数据')


with MyManager() as e:
    print(e)

# -*- coding: utf-8 -*-
# @Time    : 2018-05-02 15:37
# @Email   : Yzh_smlie@163.com
# @File    : 装饰器.py

'''
使用场景：
注入参数（提供默认参数，生成参数）
记录函数行为（日志、缓存、计时什么的）
预处理／后处理（配置上下文什么的）
修改调用时的上下文（线程异步或者并行，类方法）
'''
import time


# def c_time(func):
#     def inner():
#         begin_time = time.time()
#         func()
#         end_time = time.time()
#         print('函数花费时间%f' % (end_time - begin_time))
#
#     return inner
#
#
# @c_time
# def f1():
#     for i in range(9):
#         print(i)
#
#
# f1()

'''

# '''
#
#
def baonuan(func):
    print('保暖')

    def zhexiu():
        print('遮羞')
        func()

    return zhexiu


@baonuan
def ren():

    print('人')


ren()

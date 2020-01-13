# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 18:48
# @Email   : Yzh_smlie@163.com
# @File    : 函数中args和kwargs.py

# func(*args,**kwargs)
"""
这是Python函数可变参数 args及kwargs
*args表示任何多个无名参数，它是一个tuple
**kwargs表示关键字参数，它是一个dict
"""


def foo(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)
    print('**********************')


if __name__ == '__main__':
    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo(1, 'b', 'c', a=1, b='b', c='c')

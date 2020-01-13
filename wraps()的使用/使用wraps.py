# !/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
"""
因为当使用装饰器装饰一个函数时，函数本身就已经是一个新的函数；即函数名称或属性产生了变化。所以在python的functools模块中提供了
wraps装饰函数来确保原函数在使用装饰器时不改变自身的函数名及应有属性。
所以在装饰器的编写中建议加入wraps确保被装饰的函数不会因装饰器带来异常情况。
"""


def my_decorator(func):
    @wraps(func)              # 唯一的区别是这里加了一个装饰器,函数的名称及备注信息就不会发生更改了
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def test():
    """Testword"""
    print('Test function')


print(test.__name__, test.__doc__)         # test Testword
# print(test())






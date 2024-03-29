# !/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
from functools import wraps

"""
通过inspect模块获取函数
"""

"""
# r直接反应对象本体。,  ！符号，这个只在fromat中有用，要注意方法。但是效果类似
参考:https://blog.csdn.net/a19990412/article/details/80149112
"""


def get_func_params(func):
    # 使用inspect模块，简单方便
    params = {}
    # func = func.__wrapped__ if hasattr(func, '__wrapped__') else func   # 这个地方对于多个装饰器函数不起作用
    if not callable(func):
        return '{!r} is not a callable object'.format(func)   # r直接反应对象本体。
        # raise TypeError('{!r} is not a callable object'.format(func))
    while hasattr(func, '__wrapped__'):
        print("这个函数有几个装饰器,这里就会被打印几次")
        func = func.__wrapped__
    func_input_args = inspect.getfullargspec(func)
    print("func_input_args:", func_input_args)
    arg_name_list = list(func_input_args.args)
    print("arg_name_list:", arg_name_list)
    default_value_list = [None] * (len(func_input_args.args or tuple()) - len(func_input_args.defaults or tuple())) \
                         + list(func_input_args.defaults or tuple())
    print("default_value_list:", default_value_list)
    for k, v in zip(arg_name_list, default_value_list):
        if "log" != k:
            params.update({k: v if v else ""})
    if 'self' in params:
        params.pop('self')
    print(params)
    return params


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


def logit2(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit2
@logit
def cat(host, passwd=None, user="root"):
    pass


params = get_func_params(cat)
print("参数:", params)
print(cat.__defaults__)

print("---------------------------")

"""
@property装饰的函数,版本都是返回类的一个属性, 它的类型为<class 'property'>, not callable
"""


class B(object):
    @property
    def ss(self):
        return "这个是函数的属性"

    @staticmethod
    def sss(aaa="aaa"):
        print(aaa)


params = get_func_params(B.sss)
print("参数1:", params)

params = get_func_params(B.ss)
print("参数2:", params)

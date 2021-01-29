# !/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
from functools import partial, wraps


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


"""
http://codingdict.com/sources/py/inspect/3148.html
inspect.ismethod（object）   如果对象是用Python编写的绑定或未绑定方法，则返回true。
inspect.isfunction（object）  如果对象是Python函数，则返回true，其中包括由lambda表达式创建的函数。
"""


def getargspec(func):
    """Like inspect.getargspec but supports functools.partial as well."""
    if inspect.ismethod(func):
        func = func.__func__
    if type(func) is partial:
        orig_func = func.func
        argspec = getargspec(orig_func)
        args = list(argspec[0])
        defaults = list(argspec[3] or ())
        kwoargs = list(argspec[4])
        kwodefs = dict(argspec[5] or {})
        if func.args:
            args = args[len(func.args):]
        for arg in func.keywords or ():
            try:
                i = args.index(arg) - len(args)
                del args[i]
                try:
                    del defaults[i]
                except IndexError:
                    pass
            except ValueError:  # must be a kwonly arg
                i = kwoargs.index(arg)
                del kwoargs[i]
                del kwodefs[arg]
        return inspect.FullArgSpec(args, argspec[1], argspec[2],
                                   tuple(defaults), kwoargs,
                                   kwodefs, argspec[6])
    """这个地方相当于递归获取函数最终的函数"""
    while hasattr(func, '__wrapped__'):
        func = func.__wrapped__
    if not inspect.isfunction(func):
        raise TypeError('%r is not a Python function' % func)
    return inspect.getfullargspec(func)


para = getargspec(cat)
print(para)

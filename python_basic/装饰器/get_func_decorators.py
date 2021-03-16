# !/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import json
import time
from functools import wraps


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


@logit
@logit2
def test():
    print("111111")


def getsource(function):
    """
    其getsource函数，就是用来查看对象的源码。
    它的方便之处在于，你不用去很费劲地寻找源码所在的位置，用inspect.getsource直接将源码显示出来,
    想知道引入对象的文件也可以，用inspect.getfile

    Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
    则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

    Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
    如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    :param function:
    :return:
    """

    source = inspect.getsource(function)
    print("source_code:", source)
    file_path = inspect.getfile(function)
    print("file_path:", file_path)
    index = source.find("def ")
    print("index:", index)
    a = source[:index].strip().splitlines()
    print("a:", a)


def get_decorators(function):
    """Returns list of decorators names

    Args:
        function (Callable): decorated method/function

    Return:
        List of decorators as strings

    Example:
        Given:

        @my_decorator
        @another_decorator
        def decorated_function():
            pass

        get_decorators(decorated_function)
        ['my_decorator', 'another_decorator']

    """
    source = inspect.getsource(function)
    index = source.find("def ")
    return [
        line.strip().split()[0][1:]
        for line in source[:index].strip().splitlines()
        if line.strip()[0] == "@"
    ]


if __name__ == '__main__':
    getsource(test)
    print("*" * 100)
    decorate = get_decorators(test)
    print(decorate)

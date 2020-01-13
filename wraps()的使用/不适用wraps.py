# !/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


def my_decorator(func):
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Decorated function...')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def test():
    """Testword"""
    print('Test function')


print(test.__name__, test.__doc__)        # wrapper decorator
print(test())             # Decorated function...          Test function               None

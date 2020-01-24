# -*- coding: utf-8 -*-
# @Time    : 2018-05-18 14:39
# @Email   : Yzh_smlie@163.com
# @File    : 静态方法和类方法.py


def foo(x):
    print("executing foo(%s)" % (x))


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()


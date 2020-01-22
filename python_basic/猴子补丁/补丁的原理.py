# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""所谓的猴子补丁，是指在运行时修改类或模块，而不去改变源码，达到hot patch的目的。"""


class Foo(object):
    def bar(self):
        print("foo.bar")


def bar(self):  # 这是补丁
    print("test")


Foo().bar()
Foo.bar = bar  # 给Foo的方法打补丁,即运行时修改类的方法
Foo().bar()

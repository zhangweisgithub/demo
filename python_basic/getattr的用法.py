# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""返回对象属性值:getattr(object,name[,default]),default为默认参数,如果不提供改参数,在没有对应属性时,会出发AttributeError"""


class A(object):
    bar = 1


a = A()
print(getattr(a, "bar"))
print(getattr(a, "bar2", 2))     # 属性bar2不存在,则会返回一个默认值2












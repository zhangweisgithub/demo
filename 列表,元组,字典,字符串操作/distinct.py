# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""copy与deepcopy:copy相当于第一层的copy,更深层次采用的是引用地址的方式,deepcopy相当于开辟了一个新的内存空间"""
"""distinct()用于对得到的数据进行去重"""
import copy
list1 = ["hello", "world",["asf","asfd"], "hello", "python"]
a = copy.copy(list1)
b = copy.deepcopy(list1)
list1[2][0] = "wode"
print(a)
print(b)


"""instance(obj, basestring) == instance(obj, (str, unicode))"""
d = u"hello"
c = isinstance(d, str)
print(type(d))
print(c)


f = "name"
g = "zhangwei"
h = ("%{0}%:{1}".format(f, g))
print(h)


# 设置一些对象供别人调用
args = {"a":2}
class C:
    def c(self):
        print("我是函数C中的结果")

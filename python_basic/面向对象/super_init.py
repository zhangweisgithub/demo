# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
此时B已经成功继承了父类的属性，所以super().__init__()的作用也就显而易见了，就是执行父类的构造函数，使得我们能够调用父类的属性。
如果不适用super, 我们只能使用父类的方法,不能使用父类的属性
参考文章:https://boniu.blog.csdn.net/article/details/107802103
super详解:
https://www.runoob.com/w3cnote/python-super-detail-intro.html
"""


class A(object):
    def __init__(self, test1, test2):
        self.test1 = test1
        self.test2 = test2
        print("test1:", test1)

    def print_test(self):
        print("test2:", self.test2)


class B(A):
    def __init__(self, test1, test2, test3):
        super().__init__(test1, test2)
        self.test3 = test3


b = B(1, 2, 3)
b.print_test()
print(b.test2)

"""
test1: 1
test2: 2
2
"""

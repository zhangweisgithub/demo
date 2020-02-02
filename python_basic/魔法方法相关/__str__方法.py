# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__str__()方法
如果直接print打印对象，会看到创建出来的对象在内存中的地址
当使用print（xx）输出对象的时候，只要对象定义了__str__(self)方法，就会 打印该方法return的信息描述
__str__方法需要返回一个字符串，当做这个对象的描写
"""


class Cat:
    """定义一个猫类"""

    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name = new_name
        self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用

    def __str__(self):
        """返回一个对象的描述信息"""
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)

    def eat(self):
        print("%s在吃鱼...." % self.name)

    def drink(self):
        print("%s在喝可乐..." % self.name)

    def introduce(self):
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))


# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)

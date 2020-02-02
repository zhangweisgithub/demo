# -*- coding: utf-8 -*-
# @Time    : 2018-05-09 17:32
# @Email   : Yzh_smlie@163.com
# @File    : -new-和-init-.py


'''
__new__是一个静态方法,而__init__是一个实例方法.
__new__方法会返回一个创建的实例,而__init__什么都不返回.
只有在__new__返回一个cls的实例时后面的__init__才能被调用.
当创建一个新实例时调用__new__,初始化一个实例时用__init__.
'''


# 创建单例时，只执行1次init方法
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(18, "xxx")
b = Singleton(8, "xxx")

print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age = 19
print(b.age)

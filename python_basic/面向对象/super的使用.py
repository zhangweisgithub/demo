# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
直白的说super().__init__()，就是继承父类的init方法，同样可以使用super()点 其他方法名，去继承其他方法。

"""


# 第一层: 先写一个父类A
class A:
    def __init__(self):
        print('A')


# 第二层: 让 B、C、D 继承自A
class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(A):
    def __init__(self):
        print('D')
        super().__init__()


# 第三层： E、F、G 继承
class E(B, C):
    def __init__(self):
        print('E')
        super().__init__()


class F(C, D):
    def __init__(self):
        print('F')
        super().__init__()


class G(E, F):
    def __init__(self):
        print('G')
        super().__init__()


g = G()  # G E B F C D A      G继承自E, F是并列的，初始化的时候不会先把E初始化完毕才初始化F。


# -----------------------------------------------------------
class H:
    def add(self, x):
        y = x + 1
        print(y)


class I(H):
    def add(self, x):
        super().add(x)


b = I()
b.add(2)  # 3


# -------------------------------------------------------
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(a, b)


class SetBase(Base):
    def __init__(self, a, b, c, d):
        self.c = c
        self.d = d
        super().__init__(a, b)


set = SetBase(1, 2, 3, 4)

print("----------------------------")


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name1(self, name):  # 定义方法名时不要和变量名一样，否则在调用的时候可能会报错。
        print('方法中名字 %s' % name)
        print('类中的名字 %s' % self.name)

    def age1(self, age):
        print('方法中的年龄 %s' % age)
        print('类中的年龄 %s' % self.age)


class New_person(Person):
    def __init__(self, new_name, new_age, sex):
        super().__init__(new_name, new_age)
        self.sex = sex

    def diaoyong(self, name, age):
        self.name1(name)
        self.age1(age)

    def sex1(self, sex):
        print('方法中的性别 %s' % sex)
        print('类中的性别 %s' % self.age)


new_p = New_person('小花', '20', '男')
new_p.diaoyong('小米', '15')
new_p.sex1('女')
# new_p.name1('xiaohua')

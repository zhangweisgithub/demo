# !/usr/bin/env python
# -*- coding: utf-8 -*-


def demo(name: str, age: 'int > 0' = 20, hobbit: str = "爱好打篮球") -> str:  # ->str 表示该函数的返回值是str类型的
    print(name, type(name))
    print(age, type(age))
    print(hobbit, type(hobbit))
    return "hello world"


demo(1, 2)  # 这里的参数1会显示黄色, 但是可以运行不会报错
demo('小小', 2)  # 正常显示

"""
    以上是注解表达式的应用方法, 注解中最常用的就是  类(str 或 int )类型 和 字符串(如 'int>0')  

    注解不会做任何处理, 只是存储在函数的__annotations__属性(1个字典)中   return 返回的值的注解

    对于注解, python不做检查, 不做强制, 不做验证, 什么操作都不做.  换而言之, 注释对python解释器没有任何意义, 只是为了方便使用函数的人  
"""
print(demo.__annotations__)  # {'name': <class 'str'>, 'age': 'int > 0', 'return': <class 'str'>}


"""
函数参数注解
"""

def add(x, y:int) -> int:
    return x+y

print(add.__annotations__)
ret = add(12, 24)
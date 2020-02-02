# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建单例时，只执行1次init方法
"""


class ShoppingCart:
    """购物车类"""
    __instance = None  # 这个类属性用来记录创建好的实例对象
    __has_init = False  # 记录init方法是否已经被调用

    def __new__(cls, *args, **kwargs):  # 静态方法,没有传递cls,自动调用
        if cls.__instance is None:  # 让object的new方法只能执行一次
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if ShoppingCart.__has_init is False:
            self.total_price = 200
            ShoppingCart.__has_init = True


cart1 = ShoppingCart()
cart1.total_price = 5
# print(cart1.total_price)    # 定义价格为5,输出为5

cart2 = ShoppingCart()  # 当创建第二个对象时,由于条件限制,此时不会再进入init,价格还是5
# cart2.total_price = 2       #

print(cart1.total_price)
print(cart2.total_price)

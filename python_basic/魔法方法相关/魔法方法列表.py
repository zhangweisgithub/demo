# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
a.基本魔法方法:
    1.__new__(cls[,...])
        a.__new__ 是在一个对象实例化的时候所调用的第一个方法.
        b.它的第一个参数是这个类,其他的参数是用来直接传递给__init__方法.
        c.__new__ 决定是否使用该__init__方法,因为__new__可以调用其他类的构造方法或者直接返回别的实例化对象来作为本类的实例,
            如果__new__没有返回实例对象,则__init__不会被调用.
        d.__new__ 主要是用于继承一个不可变的类型,不如一个tuple或者string

    2.__init__(self[,...]) 构造器,当一个实例被创建的时候调用的初始化方法
    3.__del__(self) 析构器,当一个实例被销毁的时候调用的方法
    4.__call__(self[,args...]) 允许一个类的实例像函数一样被调用: x(a,b) 调用 x.__call__(a,b)
    5.__len__(self) 定义当被 len() 调用时的行为
    6.__repr__(self) 定义当被 repr() 调用时的行为
    7.__str__(self) 定义当被 str() 调用时的行为
    8.__bytes__(self) 定义当被 bytes() 调用时的行为
    9.__hash__(self) 定义当被 hash() 调用时的行为
    10.__bool__(self) 定义当被 bool() 调用时的行为,应该返回的是True或者False
    11.__format__(self,format_spec) 定义当被 format() 调用时的行为

b.有关属性
    *12.__getattr__(self,name) 定义当用户试图获取一个不存在的属性时
    *13.__getattribute__(self,name) 定义当该类的属性被访问时的行为
    14.__setattr__(self,name,value) 定义当一个属性被设置时的行为
    *15.__delattr__(self,name) 定义当一个属性被删除时的行为
    16.__dir__(self,name) 定义当 dir() 被调用时的行为
    17.__get__(self,instance,owner) 定义当描述符的值被取得时的行为
    18.__set__(self,instance,value) 定义当描述符的值被改变时的行为
    19.__delete__(self,instance) 定义当描述符的值被删除时的行为

c.比较操作符
    20.__lt__(self,other) 定义小于号的行为: x<y 调用 x.__lt__(y)
    21.__le__(self,other) 定义小于等于号的行为: x<=y 调用 x.__le__(y)
    22.__eq__(self,other) 定义等于号的行为: x==y 调用 x.__eq__(y)
    23.__ne__(self,other) 定义不等号的行为: x!=y 调用 x.__ne__(y)
    24.__gt__(self,other) 定义大于号的行为: x>y 调用 x.__gt__(y)
    25.__ge__(self,other) 定义大于等于号的行为: x>=y 调用 x.__ge__(y)

d.算法运算符
    26.__add__(self,other) 定义加法的行为: +
    27.__sub__(self,other) 定义减法的算法: -
    28.__mul__(self,other) 定义乘法的行为: *
    29.__truediv__(self,other) 定义真除法的行为: /
    30.__floordiv__(self,other) 定义整数除法(地板除)的行为: //
    31.__mod__(self,other) 定义取模算法的行为: %
    32.__divmod__(self,other) 定义当被 divmod() 调用时的行为
    33.__pow__(self,other[,modulo]) 定义当被 power() 调用或**运算时的行为
    34.__lshift__(self,other) 定义按位左移的行为:<<
    35.__rshift__(self,other) 定义按位右移的行为:>>
    36.__add__(self,other) 定义按位与操作的行为:&
    37.__xor__(self,other) 定义按位异或操作的行为:^
    38.__or__(self,other) 定义按位或操作的行为:|

e.反运算
    39.__radd__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    40.__rsub__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    41.__rmul__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    42.__rtruediv__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    43.__rfloordiv__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    44.__rmod__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    45.__rdivmod__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    46.__rpow__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    47.__rlshift__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    48.__rrshift__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    49.__rxor__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用
    50.__ror__(self,other) 与上方相同,当左操作数不支持相应的操作时被调用

f.增量赋值运算
    51.__iadd__(self, other)    定义赋值加法的行为：+=
    52.__isub__(self, other)    定义赋值减法的行为：-=
    53.__imul__(self, other)    定义赋值乘法的行为：*=
    54.__itruediv__(self, other)    定义赋值真除法的行为：/=
    55.__ifloordiv__(self, other)    定义赋值整数除法的行为：//=
    56.__imod__(self, other)    定义赋值取模算法的行为：%=
    57.__ipow__(self, other[, modulo])    定义赋值幂运算的行为：**=
    58.__ilshift__(self, other)    定义赋值按位左移位的行为：<<=
    59.__irshift__(self, other)    定义赋值按位右移位的行为：>>=
    60.__iand__(self, other)    定义赋值按位与操作的行为：&=
    61.__ixor__(self, other)    定义赋值按位异或操作的行为：^=
    62.__ior__(self, other)    定义赋值按位或操作的行为：|=

g。一元操作符
    63._neg__(self)    定义正号的行为：+x
    64.__pos__(self)    定义负号的行为：-x
    65.__abs__(self)    定义当被 abs() 调用时的行为
    66.__invert__(self)    定义按位求反的行为：~x

h.类型转换
    67.__complex__(self)    定义当被 complex() 调用时的行为（需要返回恰当的值）
    68.__int__(self)    定义当被 int() 调用时的行为（需要返回恰当的值）
    69.__float__(self)    定义当被 float() 调用时的行为（需要返回恰当的值）
    70.__round__(self[, n])    定义当被 round() 调用时的行为（需要返回恰当的值）
    71.__index__(self)    1. 当对象是被应用在切片表达式中时，实现整形强制转换
                        2. 如果你定义了一个可能在切片时用到的定制的数值型,你应该定义 __index__
                        3. 如果 __index__ 被定义，则 __int__ 也需要被定义，且返回相同的值

i.上下文管理（with 语句）
    72.__enter__(self)    1. 定义当使用 with 语句时的初始化行为
                        2. __enter__ 的返回值被 with 语句的目标或者 as 后的名字绑定
    73.__exit__(self, exc_type, exc_value, traceback)
                1. 定义当一个代码块被执行或者终止后上下文管理器应该做什么
                2. 一般被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作

j.容器类型
    74.__len__(self)    定义当被 len() 调用时的行为（返回容器中元素的个数）
    75.__getitem__(self, key)    定义获取容器中指定元素的行为，相当于 self[key]
    76.__setitem__(self, key, value)    定义设置容器中指定元素的行为，相当于 self[key] = value
    77.__delitem__(self, key)    定义删除容器中指定元素的行为，相当于 del self[key]
    78.__iter__(self)    定义当迭代容器中的元素的行为
    79.__reversed__(self)    定义当被 reversed() 调用时的行为
    80.__contains__(self, item)    定义当使用成员测试运算符（in 或 not in）时的行为
"""
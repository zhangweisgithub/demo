# !/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

print(uuid.uuid1())           # 7135be1c-2f37-11e9-982c-309c231e2108
# replace() 方法用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。
print(str(uuid.uuid1()).replace("-", "_"))          # a55b59ae_2f37_11e9_98c7_309c231e2108


"""
python的uuid模块提供UUID类和函数uuid1(), uuid3(), uuid4(), uuid5() 来生成1, 3, 4, 5各个版本的UUID 
(需要注意的是: python中没有uuid2()这个函数). 对uuid模块中最常用的几个函数总结如下: 

　　1.  uuid.uuid1([node[, clock_seq]])  : 基于时间戳
　　使用主机ID, 序列号, 和当前时间来生成UUID, 可保证全球范围的唯一性. 但由于使用该方法生成的UUID中包含有主机的网络地址, 因此可能危及隐私. 
   该函数有两个参数, 如果 node 参数未指定,系统将会自动调用 getnode() 函数来获取主机的硬件地址. 
   如果 clock_seq  参数未指定系统会使用一个随机产生的14位序列号来代替. 

　　2.  uuid.uuid3(namespace, name) : 基于名字的MD5散列值
　　通过计算命名空间和名字的MD5散列值来生成UUID, 可以保证同一命名空间中不同名字的唯一性和不同命名空间的唯一性, 
    但同一命名空间的同一名字生成的UUID相同.

　　4.  uuid.uuid4() : 基于随机数
　　通过随机数来生成UUID. 使用的是伪随机数有一定的重复概率. 

　　5.  uuid.uuid5(namespace, name) : 基于名字的SHA-1散列值
　　通过计算命名空间和名字的SHA-1散列值来生成UUID, 算法与 uuid.uuid3() 相同.
"""
# -*- coding: utf-8 -*-
# @Time    : 2018-04-28 10:34
# @Email   : Yzh_smlie@163.com
# @File    : 拷贝问题.py

import copy

a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)

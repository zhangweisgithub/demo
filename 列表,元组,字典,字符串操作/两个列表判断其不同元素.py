# !/usr/bin/env python
# -*- coding: utf-8 -*-
a = [1, 2, 3, 4]
b = [1, 2, 3, 4, 5]

m = [x for x in a if x in b]
print("same:", m)

n = [y for y in (a+b) if y not in b]
k = [y for y in (a+b) if y not in a]
print(n)
print(k)


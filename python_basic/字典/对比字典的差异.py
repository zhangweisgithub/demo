# !/usr/bin/env python
# -*- coding: utf-8 -*-
dict1 = {1: 1, 2: 2, 3: 3}
dict2 = {1: 1, 2: 2, 4: 5}
differ = list(set(dict1.items()) ^ set(dict2.items()))
print(differ)

li = list(set([i[0] for i in differ]))
print(li)

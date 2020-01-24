# -*- coding: utf-8 -*-
# 利用collections库的Counter方法统计字符串每个单词出现的次数
from collections import Counter

a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

# 统计某个字符出现的次数
ret = a.count("j")
print(ret)

# 字符串转大小写
str1 = 'HHHuuu'
print(str1.upper())
print(str1.lower())

# 两种方法去空格
str3 = 'hello word'
res1 = str3.replace(" ", " ")
print(res1)
list1 = str3.split(' ')
res2 = ''.join(list1)
print(res2)

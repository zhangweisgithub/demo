# !/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
a = "asfqaifwewfihwq;jfeibhgf"
res = Counter(a)
print(res)     # Counter({'f': 5, 'i': 3, 'w': 3, 'a': 2, 'e': 2, 'h': 2, 'q': 2, 'b': 1, 'g': 1, 'j': 1, 's': 1, ';': 1})


# 提供计数器工具以支持方便快捷的计数
cnt = Counter()
for world in ["red","blue","green","blue","red","red","green","red","blue","red","red""blue","green"]:
    cnt[world] += 1
print(cnt)     # Counter({'red': 5, 'blue': 3, 'green': 3, 'redblue': 1})




















# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
s = "<a>hah</a><a>heh</a>"
res1 = re.findall("<a>(.*)</a>", s)
print ("贪婪匹配:", res1)

res2 = re.findall("<a>(.*?)</a>", s)
print ("非贪婪匹配:", res2)

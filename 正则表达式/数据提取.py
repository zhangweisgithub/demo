# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的"""


import re
str = '<div class="name">中国</div>'
# .代表可有可无,*代表任意字符      (.*?)提取文本
res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)


# 数据替换
a = "张明 93分"
ret = re.sub(r"\d+", "100", a)
print(ret)

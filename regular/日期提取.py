# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 匹配日期  2018-03-20
import re
url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
result = re.findall(r'dateRange=(.*?)%7C(.*?)&', url)
print(result)
result1 = re.findall(r"y/(.*?)/get", url)
print(result1)

"""
.  是任意字符 可以匹配任何单个字符
.*？  表示匹配任意字符到下一个符合条件的字符
例子：正则表达式a.*?xxx   可以匹配 abxxx  axxxxx  abbbbbxxx

字符  URL编码

空格   %20
&        %26
%       %25
:         %3A
|         %7C
"""
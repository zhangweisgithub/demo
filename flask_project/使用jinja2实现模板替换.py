# !/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Template

"""
使用模板替换的功能
"""

template = Template('Hello {{ name }}!')
print(template.render(name='World'))

a = {"key": {"host": "10.9.244.33"}}
temp = Template("`<key.host>`", variable_start_string="`<", variable_end_string=">`")
print(temp.render(a))

"""
Hello World!
10.9.244.33
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template

tpl = Template('my name is : {{ name }}, `< old >`', variable_start_string="`<", variable_end_string=">`")
text = tpl.render(name='jack', old=18)
print(text)           # my name is : jack, 18


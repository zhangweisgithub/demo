# !/usr/bin/env python
# -*- coding: utf-8 -*-
with open("test.txt", "a", encoding="utf8") as pyfile:
    content = pyfile.write("safd按时发大水1")
    print(content)

with open("test.txt", "r", encoding="utf-8") as pyfile:
    content = pyfile.read()
    print(content)


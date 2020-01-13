# !/usr/bin/env python
# -*- coding: utf-8 -*-

#
# with open("获取路径下所有的py文件.py", "r") as pyfile:
#     content = pyfile.read()
#     # content = "\n".join(content)
#     print(content)



with open("test.txt", "a", encoding="utf8") as pyfile:
    content = pyfile.write("safd按时发大水")
    # content = "\n".join(content)
    print(content)



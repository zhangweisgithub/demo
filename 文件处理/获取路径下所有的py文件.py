# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ["HOME_PATH"] = os.path.split(os.path.realpath(__file__))[0]
print(os.environ["HOME_PATH"])
# def get_py_file():
#     HOME = os.environ.get("HOME_PATH")
#     if os.path.isdir(HOME):
#         print("1")
#
#
# get_py_file()

test = os.path.join(os.environ["HOME_PATH"], "test.py")
print(test)
if os.path.exists(test):
    os.remove(test)
else:
    print("test")


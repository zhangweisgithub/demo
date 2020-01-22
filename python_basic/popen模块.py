# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

# 使用 mkdir 命令
a = 'mkdir nwdir'

b = os.popen(a, 'r', 1)

print(b)


from subprocess import Popen, PIPE, STDOUT
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
command = "echo 'hello linux world!'"
p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False, cwd=currentPath)
output, errors = p.communicate()
if errors:
    print(errors)
print(output)

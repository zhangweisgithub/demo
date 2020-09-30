# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import subprocess
import os


def get_all_pre_funcs():
    print(os.getcwd())
    status, ret = subprocess.getstatusoutput("python3 %s" % os.path.join(os.getcwd(), "task1.py"))
    if status == 1:
        return "Traceback:Syntax Error Params, msg: " + ret
    elif status == 2:
        print("文件路径错误!")
        return "文件路径错误"
    print(f"状态:{status}, 结果：{ret}")


if __name__ == '__main__':
    get_all_pre_funcs()

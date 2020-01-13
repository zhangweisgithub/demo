# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import subprocess
import os
import traceback

from flask import json


def get_all_pre_funcs():
    print(os.getcwd())
    status, ret = subprocess.getstatusoutput("python %s" % "D:\\platform\\demo\\创建一个临时文件\\demo.py")
    status, ret = subprocess.getstatusoutput("python %s" % "D:\\platform\\demo\\创建一个临时文件\\项目中的内容.py")
    print("结果：", status, ret)
    if status == 1:
        print("错误")
        return "Traceback: Get SetupTears with Syntax Error Params, msg: " + ret
    func_ret_base64 = ret.split("Start:")[-1].split(":End")[0].encode("utf-8")
    try:
        result = json.loads(base64.b64decode(func_ret_base64))
    except:
        result = []
    try:
        os.remove("")
    except Exception as e:
        # self.log.error(traceback.format_exc())
        print(e)
    print(result)
    return result


if __name__ == '__main__':
    get_all_pre_funcs()

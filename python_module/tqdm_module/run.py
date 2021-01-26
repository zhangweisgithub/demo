# !/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys

"""
可以在这个地方指定python执行的路径,但是注意在windows中这个命令可能会出现
'PYTHONPATH' 不是内部或外部命令,也不是可运行的程序 或批处理文件
需要在linux中进行执行才是正常的
"""
sys.path.insert(0, "D:\\platform\\demo\\python_module\\tqdm_module\\test")
command = f"PYTHONPATH=D:\\platform\\demo\\python_module\\tqdm_module\\test python demo1.py"
status, ret = subprocess.getstatusoutput(command)
print(status,ret)

# import time
# from tqdm import tqdm
# from tqdm._tqdm import trange
#
# for i in tqdm(range(100)):
#     time.sleep(0.01)

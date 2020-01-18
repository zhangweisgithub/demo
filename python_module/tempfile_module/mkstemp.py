# !/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import tempfile
import os

""""
mkstemp会在路径中创建一个文件
tempfile.mkstemp()返回的第一个参数是一个fd(file_description)文件描述符，和一个包含绝对路径的文件名称。
tempfile里面的有些方法创建的文件是在关闭之后会自动删除的，但是mkstemp()这个方法创建的临时文件并不会被删除，只是不会被其他应用程序找到和使用。
你可以在使用之后通过os.close(fd)这个方法关闭这个文件。
顺便介绍一个tempfile.TemporaryFile()方法，他在创造了临时文件之后会在文件关闭之后销毁 可以尝试使用以下方法测试一下。
"""

template = """
# !/usr/bin/env python
# -*- coding: utf-8 -*-
def test():
    print("hello world")


if __name__ == '__main__':
    test()
"""


fd, temp_path = tempfile.mkstemp(prefix="temp", suffix=".py", dir=os.path.dirname(__file__), text=False)
print(fd)
print(temp_path)
with open(temp_path, "w+", encoding="utf-8") as file:
    file.write(template)  # 将内容写到临时文件中
    file.seek(0)  # 从文件的初始位置读取文件内容
    print(file.read())
status, ret = subprocess.getstatusoutput(f"python {temp_path}")
print(f"临时文件执行结果:{ret}")
os.close(fd)  # 如果不加这一句会包文件程序正在被使用无法删除的错误
try:
    os.remove(temp_path)
except Exception as e:
    print(e)

"""
[WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'C:\\Users\\ZHANGW~1\\AppData\\Local\\Temp\\tempgxwgbg7w.py'
"""

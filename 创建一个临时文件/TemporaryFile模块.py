# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import os
file_object = tempfile.TemporaryFile(dir=os.path.dirname(__file__))
with file_object as f:
    f.write(b"asfdafasdfasf")
    f.seek(0)   # 文件指针到文件的初始位置
    print(f.read())




















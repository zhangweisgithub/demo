# !/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
with zipfile.ZipFile("test.py", mode="w") as zipf:
    zipf.write("zip.py")

zipf = zipfile.ZipFile("test.py")
print(zipf.namelist())














# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
应用数据分析库pandas:python3中安装的有pandas模块
pandas应该可以读取很多相关文件的内容
"""
import pandas as pd

df = pd.read_excel("./test.xlsx")
print(df)

"""
   姓名  年龄 性别
0  张三  21  男
1  李四  32  男
2  小红  12  女
"""

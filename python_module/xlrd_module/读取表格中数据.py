# !/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

"""
对excel表格的读取,获取表格中所有的用例id
"""
data = xlrd.open_workbook('./sheet1.xlsx')  # excel文件位置
sheet = data.sheets()[4]  # 读取第4个表
rows = sheet.row_values(0)  # 读取第一行
print(rows)  # 打印第一行
clou = sheet.col_values(0)  # 读取第一列
print(clou)  # 打印第一列

x = clou[1:]  # 去除第一行的第一个数
print(x)

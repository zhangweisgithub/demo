# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Xlsx是python用来构造xlsx文件的模块，可以向excel2007+中写text，numbers，formulas 公式以及hyperlinks超链接。
可以完成xlsx文件的自动化构造，包括：
合并单元格，制作excel图表等功能
"""
import xlsxwriter
workbook = xlsxwriter.Workbook("hello.xlsx")       # 建立文件
worksheet = workbook.add_worksheet("sheet1_test")               # 建立sheet,指定sheet名
worksheet.write("A1", "hello world")              # 向A1中写入
workbook.close()



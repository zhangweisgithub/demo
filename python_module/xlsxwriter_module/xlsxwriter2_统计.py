# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""添加字体加粗"""

import xlsxwriter

filename = '2.xlsx'
test_book = xlsxwriter.Workbook(filename)
worksheet = test_book.add_worksheet('what')
bold = test_book.add_format({"bold": True})    # 先指定好添加的格式

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# 定义起始的行列 会在这个基础上 行列各加一 作为初始行列
row = 0
col = 0

for item, cost in expenses:
    worksheet.write(row, col, item, bold)    # 写入的时候可以指定定义好的格式
    worksheet.write(row, col+1, cost)
    row += 1

worksheet.write(row, col+1, '=sum(B1:B4)')
test_book.close()

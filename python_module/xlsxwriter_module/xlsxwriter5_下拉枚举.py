# !/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter

workbook = xlsxwriter.Workbook("5.xlsx")
worksheet = workbook.add_worksheet("sheet1")
headings = ["number", "test1", "test2", "test3"]

data = [
    ["2019-12-1", "2019-12-2", "2019-12-3", "2019-12-4", "2019-12-5", "2019-12-6"],
    [10, 20, 30, 40, 50, 60],
    [1, 2, 3, 4, 5, 6]
]
worksheet.write_row("A1", headings)  # 表头写入行内容
worksheet.write_column("A2", data[0])  # 按列进行填充
worksheet.write_column("B2", data[1])
worksheet.write_column("C2", data[2])
worksheet.write_column("D2", [])
worksheet.data_validation("D2:D1048576", {"validate": "list",
                                          "source": [
                                              "枚举值1",
                                              "枚举值2",
                                              "枚举值3"
                                          ]})
workbook.close()

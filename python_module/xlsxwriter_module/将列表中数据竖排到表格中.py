# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""添加字体加粗"""

import xlsxwriter

filename = 'test.xlsx'
test_book = xlsxwriter.Workbook(filename)
worksheet = test_book.add_worksheet('what')
bold = test_book.add_format({"bold": True})    # 先指定好添加的格式

expenses = (['pass_rate', 'case_id', 'start_time', 'progress', 'pass_num', 'fail_num', 'not_run_id', 'total_num',
             'duration', 'status', 'serial_no', 'path', 'end_time', 'final_result', 'case_id', 'trace_log', 'channel',
             'config', 'script_temp_path', 'current_log', 'user_config', 'db_user_config', 'db_setup_teardown',
             'chose_config', 'concurrent', 'run_set_ids', 'status', 'setup_result', 'col_setup_teardown',
             'col_setup_teardown_result', 'col_setup_teardown_gap', 'progress', 'start_time', 'collection_time_gap',
             'end_time', 'trace_log', 'tear_result', 'final_result', 'set_report', 'progress', 'status', 'start_time',
             'case_id', 'script_temp_path', 'current_log', 'pass_rate', 'pass_num', 'fail_num', 'not_run_id', 'total_num',
             'duration', 'serial_no', 'path', 'end_time', 'final_result', 'case_id', 'trace_log',
             'channel', 'config', 'script_temp_path', 'current_log']
)

# 定义起始的行列 会在这个基础上 行列各加一 作为初始行列
row = 0
col = 0

for item in expenses:
    worksheet.write(row, col+1, item)
    row += 1

test_book.close()

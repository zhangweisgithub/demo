# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")
        assert 0  # 断言失败```

"""
pytest --pyargs ./test_report.py -s --html=D:/platform/report/pytest/report.html
执行之后会在对应的路径中生成对应的报告
"""

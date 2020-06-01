# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def return_test_data():
    return [(1, 2), (0, 3)]


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的形式传入参数值
    def test_a(self, a, b):
        print("test data:a=%d,b=%d" % (a, b))
        assert a + b == 3


"""
 执行结果：
    test_abc.py
    ------->setup_class
    test
    data: a = 1, b = 2  # 运行第一次取值 a=1,b=2
    .
    test
    data: a = 0, b = 3  # 运行第二次取值 a=0,b=3
    .
    ------->teardown_class
"""

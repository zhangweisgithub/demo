# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a,b", [(1, 2), (0, 3)])  # 参数a,b均被赋予两个值，函数会运行两遍
    def test_a(self, a, b):  # 参数必须和parametrize里面的参数一致
        print("test data:a=%d,b=%d" % (a, b))
        assert a + b == 3


"""
执行结果：
    test_abc.py 
    ------->setup_class
    test data:a=1,b=2 # 运行第一次取值 a=1,b=2
    .
    test data:a=0,b=3 # 运行第二次取值 a=0,b=3
    .
    ------->teardown_class


"""

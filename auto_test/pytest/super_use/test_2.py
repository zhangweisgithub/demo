# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
标记测试函数为失败函数
 方法：
     xfail(condition=None, reason=None, raises=None, run=True, strict=False)
 常用参数：
     condition：预期失败的条件，必传参数
     reason：失败的原因，必传参数
 使用方法：
     @pytest.mark.xfail(condition, reason="xx")

"""
import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.xfail(2 > 1, reason="标注为预期失败")  # 标记为预期失败函数test_b
    def test_b(self):
        print("------->test_b")
        assert 0


"""
执行结果：
       test_abc.py 
       ------->setup_class
       ------->test_a
       .
       ------->test_b
       ------->teardown_class
       x  # 失败标记

"""

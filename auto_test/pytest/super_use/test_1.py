# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


"""
根据特定的条件，不执行标识的测试函数.
 方法：
     skipif(condition, reason=None)
 参数：
     condition：跳过的条件，必传参数
     reason：标注原因，必传参数
 使用方法：
     @pytest.mark.skipif(condition, reason="xxx") 


"""

"""
跳过测试函数


注意:如果ini文件中包含有中文,那么用例在运行的时候可能会执行失败
UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 106: illegal multibyte sequence
可能是windows在读取配置的时候的失败了
"""


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.skipif(condition=2 > 1, reason="跳过测试函数")  # 跳过测试函数test_b
    def test_b(self):
        print("------->test_b")
        assert 0


"""
执行结果：
test_abc.py
------->setup_class
------->test_a  # 只执行了函数test_a
.
------->teardown_class
s  # 跳过函数```
"""

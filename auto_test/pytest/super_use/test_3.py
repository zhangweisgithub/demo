# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
方便测试函数对测试属于的获取。
 方法：
     parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
 常用参数：
     argnames：参数名
     argvalues：参数对应值，类型必须为list
                 当参数为一个时格式：[value]
                 当参数个数大于一个时，格式为:[(param_value1,param_value2.....),(param_value1,param_value2.....)]
 使用方法:
     @pytest.mark.parametrize(argnames,argvalues)
     ️ 参数值为N个，测试方法就会运行N次
"""
import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a", [3, 6])  # a参数被赋予两个值，函数会运行两遍
    def test_a(self, a):  # 参数必须和parametrize里面的参数一致
        print("test data:a=%d" % a)
        assert a % 3 == 0


"""

    执行结果:
    test_abc.py 
    ------->setup_class
    test data:a=3 # 运行第一次取值a=3
    .
    test data:a=6 # 运行第二次取值a=6
    . 
    ------->teardown_class

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: test_abc.py
import pytest  # 引入pytest包


def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


"""
断言:如果后面的数据为false的话,就会抛出AssertionError
"""


def test_b():
    print("------->test_b")
    assert 0  # 断言失败


@pytest.mark.slow
def test_c():  # test开头的测试函数
    print("------->test_c")
    assert 1  # 断言成功

if __name__ == '__main__':
    pytest.main("-s  test_abc.py")  # 调用pytest的main函数执行测试

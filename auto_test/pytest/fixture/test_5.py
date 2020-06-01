# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='class', autouse=True)  # 作用域设置为class，自动运行
def before():
    print("------->before")


class Test_ABC:
    def setup(self):
        print("------->setup")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")
        assert 1


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")
"""
设置作用域为class
执行结果：
    test_abc.py
    ------->before # 发现只运行一次
    ------->setup
        ------->test_a
        .
        ------->setup
        ------->test_b
        .

"""

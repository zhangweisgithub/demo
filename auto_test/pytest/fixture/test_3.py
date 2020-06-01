# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(autouse=True)  # 设置为默认运行
def before():
    print("------->before")


class Test_ABC:
    def setup(self):
        print("------->setup")

    def test_a(self):
        print("------->test_a")
        assert 1


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")

"""
默认设置为运行
执行结果：
    test_abc.py 
    ------->before # 发现before自动优先于测试类运行
    ------->setup
    ------->test_a
        .
"""

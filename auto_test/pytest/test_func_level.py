# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_ABC:
    # 函数级开始
    def setup(self):
        print("------->setup_method")

    # 函数级结束
    def teardown(self):
        print("------->teardown_method")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")


"""
这种函数级别的setup, teardown在运行的时候,每个用例执行的时候都会去执行一次setup,teardown
pytest --pyargs ./test_func_level.py -s
执行结果:
test_func_level.py ------->setup_method
------->test_a
.------->teardown_method
------->setup_method
------->test_b
.------->teardown_method


"""
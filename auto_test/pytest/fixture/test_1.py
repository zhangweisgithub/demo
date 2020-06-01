# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_ABC:
    @pytest.fixture()
    def before(self):
        print("------->before")

    def test_a(self, before):  # ️ test_a方法传入了被fixture标识的函数，已变量的形式
        print("------->test_a")
        assert 1


if __name__ == '__main__':
    pytest.main("-s  test_1.py")

"""
通过参数引用
fixture\test_1.py ------->before     # 发现before会优先于测试函数运行
------->test_a
"""



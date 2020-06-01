# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture()
def need_data():
    return 2  # 返回数字2


class Test_ABC:

    def test_a(self, need_data):
        print("------->test_a")
        assert need_data != 3  # 拿到返回值做一次断言


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")

"""
返回值
执行结果：
test_abc.py
------->test_a
.
``

"""

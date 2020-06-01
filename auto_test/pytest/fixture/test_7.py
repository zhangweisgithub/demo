# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[1, 2, 3])
def need_data(request):  # 传入参数request 系统封装参数
    return request.param  # 取列表中单个值，默认的取值方式


class Test_ABC:

    def test_a(self, need_data):
        print("------->test_a")
        assert need_data != 3  # 断言need_data不等于3


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")


"""
执行结果：
# 可以发现结果运行了三次
test_abc.py
1
------->test_a
.
2
------->test_a
.
3
------->test_a
F
"""

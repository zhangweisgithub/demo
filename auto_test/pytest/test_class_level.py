# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class Test_ABC:
    # 测试类级开始
    def setup_class(self):
        print("------->setup_class")

    # 测试类级结束
    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    def test_b(self):
        print("------->test_b")
        if __name__ == '__main__':
            pytest.main("-s  test_abc.py")


"""
这里,相当于是setup只执行一次,然后teardown也只执行一次(不管有多少个函数)
执行结果：
  ------->setup_class # 第一次 setup_class()
  ------->test_a
  .
  ------->test_b
  F 
          ------->teardown_class # 第一次 teardown_class()

"""

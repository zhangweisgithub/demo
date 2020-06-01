# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()  # fixture标记的函数可以应用于测试类外部
def before():
    print("------->before")


@pytest.mark.usefixtures("before")
class Test_ABC:
    def setup(self):
        print("------->setup")

    def test_a(self):
        print("------->test_a")
        assert 1


if __name__ == '__main__':
    pytest.main("-s  test_abc.py")

"""
通过函数引用
  执行结果：
      test_abc.py 
      ------->before # 发现before会优先于测试类运行
      ------->setup
      ------->test_a
      .

"""

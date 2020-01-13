# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from time与datetime import time

""" 我们利用这一特性在自动化中setup主要是进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值，数据库操作等等
 teardown是测试后的清除工作，比如参数还原或销毁，数据库的还原恢复等
执行顺序如下：setUp---test_001---setUp---test_002---tearDown
 """


class Buy_Broject_Establish(unittest.TestCase):         # 第二步创建继承一个unittest.TestCase的类
    def setUp(self):            # 第三步定义一个setup，放一些准备的工作，或者准备一些测试数据。
        print("setup")
        time.sleep(2)

    def test_001(self):         # 进入登录页面
        print("test__001")
        time.sleep(2)

    def test_002(self):         # 进入收购项目管理首页
        print("test__002")
        time.sleep(2)

    def tearDown(self):         # 第三步：定义一个tearDown，当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
            print("teardown")


if __name__ == '__main__':      # 如果其他的类调用的这个类的时候他就会自动忽略掉这个函数，他是为了测试自身的类用的
    unittest.main()             # 启动程序


# 得到如下的打印结果:
"""
setup
test__001
.teardown
setup
test__002
teardown
.
----------------------------------------------------------------------
Ran 2 tests in 8.001s

OK
"""
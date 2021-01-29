# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
with关键字和上下文管理器
https://blog.csdn.net/u010339879/article/details/103340517

什么是上下文管理器？
任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器
实现了 __enter__() 和 __exit__() 方法的对象就可以使用 with 语句

上下文管理的作用 和 目的
上下文管理 对象 是为了存在的目的 是管理 with 语句, 而 with 语句 目的是为了 简化 tyr/ finally 这种模式
这种 模式 保证 运行 一段代码后, ,即便代码里面发生错误, return 语句或者调用 终止 sys.exit() , 也会执行特定的代码段, 来做一些最后的处理 , 比如 释放连接, 还原一些状态,释放资源等 .

上下文管理器的实现
实现一个上下文管理器，必须实现两个魔法方法 __enter__() 和 __exit__()方法
不管以哪种方式 退出 with 语句, 都会进行 __enter__ 方法里面的代码段
"""


class MyManager:
    def __enter__(self):
        print('连接资源')
        return self  # 注意必须返回self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出连接')

    def show(self):
        print('资源数据')


with MyManager() as e:
    e.show()

# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Resource:
    def __enter__(self):
        print("connect to resource")
        return "frank"
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type: 异常类
        :param exc_val: 异常值
        :param exc_tb:  traceback 对象
        :return:
        """
        print(exc_type, exc_val, exc_tb)
        print("close resource  connection")

    def query(self):
        print("query  data ...")


with Resource() as r:
    1 / 0
    print(f"r:{r}")

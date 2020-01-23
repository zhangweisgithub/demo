# !/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_data(di):
    """
    :param di: 输入参数的params为字典
    :return:
    """
    for k in list(di.keys()):
        if di[k] is None:
            di.pop(k)
    return "".join(["{0}={1}&".format(k, di[k]) for k in sorted(di.keys())])[:-1]     # [:-1],把字符串的最后一个&切掉


if __name__ == '__main__':
    a = {"test": "test1", "abc": "test2", "def": "test3", "sf": None}
    res = sort_data(a)
    print(res)     # abc=test2&def=test3&test=test1

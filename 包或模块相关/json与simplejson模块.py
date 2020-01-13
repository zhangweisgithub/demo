# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simplejson适用性更广,python3中如下代码不能再适用json了
"""
import simplejson

content = {"test": "asfds"}


def decode_str(content, encoding="utf-8"):
    """
    :param content:
    :param encoding:
    :return:
    """
    # 只支持json格式
    # indent 表示缩进空格数
    return simplejson.dumps(content, encoding=encoding, ensure_ascii=False, indent=4)


c = decode_str(content)
print(c)

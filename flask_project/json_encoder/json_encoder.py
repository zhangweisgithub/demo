# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python 处理 JSON 数据时，dumps 函数是经常用到的，当 JSON 数据中有特殊类型时，往往是比较头疼的，因为经常会报这样一个错误。
原因在于 dumps 函数不知道如何处理 datetime 对象，默认情况下 json 模块使用 json.JSONEncoder 类来进行编码，此时我们需要自定义一下编码类。
"""
import json
from datetime import datetime

USER_DATA = dict(
    id=1, name='wxnacy', ts=datetime.now()
)
print(json.dumps(USER_DATA))




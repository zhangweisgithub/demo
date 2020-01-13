# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime

"""
 dumps 函数不知道如何处理 datetime 对象，默认情况下 json 模块使用 json.JSONEncoder 类来进行编码，此时我们需要自定义一下编码类。
"""


class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        if isinstance(x, datetime):
            return int(x.timestamp())
        return super().default(self, x)


USER_DATA = dict(
    id=1, name='wxnacy', ts=datetime.now()
)
print(json.dumps(USER_DATA, cls=CustomEncoder))  # 最后整合起来，将类使用 cls 参数传入 dumps 函数即可。
# {"id": 1, "name": "wxnacy", "ts": 1562938926}

a = datetime.now()
print(a)  # 2019-10-12 18:42:04.689900
print(int(a.timestamp()))  # 将数据变成了一个时间戳（timestamp)


"""
使用 CustomEncoder 实例的 encode 函数可以对对象进行转码
"""
print(CustomEncoder().encode(datetime.now()))          # 1570877111

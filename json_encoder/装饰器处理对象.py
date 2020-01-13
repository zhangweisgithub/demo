# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CustomEncoder 如果处理的对象种类很多的话，需要写多个 if elif else 来区分，这样并不是不行，但是不够优雅，不够 pythonic

根据对象的类型不同，而做出不同的处理。刚好有个装饰器可以做到这点，它就是单分派函数 functools.singledispatch
"""
import json
from datetime import datetime
from datetime import date
from functools import singledispatch


class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        try:
            return encode(x)
        except TypeError:
            return super().default(self, x)


@singledispatch  # 1
def encode(x):
    raise TypeError('Unencode type')


@encode.register(datetime)  # 2
def _(x):
    return int(x.timestamp())


@encode.register(date)
def _(x):
    return x.isoformat()


print(dict(dt=datetime.now(), d=date.today()))
# {'dt': datetime.datetime(2019, 10, 12, 18, 50, 11, 863058), 'd': datetime.date(2019, 10, 12)}
print(json.dumps(dict(dt=datetime.now(), d=date.today()), cls=CustomEncoder))
# {"dt": 1562940781, "d": "2019-07-12"}


"""
国际标准化组织的国际标准ISO 8601是日期和时间的表示方法

"""
import datetime

# 本地ISO时间
a = datetime.datetime.now().isoformat()  # 2019-10-12T18:56:26.276529
print(a)

# UTC改为ISO-8601：
b = datetime.datetime.utcnow().isoformat()
print(b)                               # 2019-10-12T10:57:59.732422

# 本地到ISO-8601没有微秒：
import datetime
c = datetime.datetime.now().replace(microsecond=0).isoformat()
print(c)                              # 2019-10-12T18:58:49

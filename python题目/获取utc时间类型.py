# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from pyrfc3339 import generate


def get_UTC_time(forward_days):
    now = datetime.datetime.now()
    new_time = now + datetime.timedelta(days=forward_days)
    end_time = generate(new_time, accept_naive=True, microseconds=True)
    print(end_time)


get_UTC_time(1)
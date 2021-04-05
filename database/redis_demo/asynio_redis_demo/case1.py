# !/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import time

import redis
import random
import json
import ast


def set_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    for i in range(1000):
        value = json.dumps(
            {"a": random.randint(1, 10), "b": "*" * 1000, "c": "*" * 10000, "d": "*" * 1000, "e": "*" * 1000,
             "f": "*" * 1000})
        progress_key = f"progress:set_{i}"
        str.set(progress_key, value)


def get_data():
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    total = 0
    st = time.time()
    for i in range(10):
        progress_key = f"progress:set_{i}"
        time.sleep(0.1)
        progress_value = str.get(progress_key)
        progress_value = ast.literal_eval(progress_value)
        a = progress_value.get('a')
        total += a
    et = time.time()
    print("耗时:", et-st)
    return total


if __name__ == '__main__':
    # set_data()
    total = get_data()
    print(total)

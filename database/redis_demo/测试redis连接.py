# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import random
import json
import time
import ast


def set_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=1, password="ODhzdElWQTIwMTc=")
    print(str)
    for i in range(10):
        value = json.dumps({"a": random.randint(1, 10), "b": "*" * 1000, "c": "*" * 1000, "d": "*" * 1000})
        str.set(f"set_{i}", value)
    # print("RESULT:", result)


def get_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=1, password="ODhzdElWQTIwMTc=")
    print(str)
    total = 0
    st = time.time()
    for i in range(10):
        result = str.get(f"set_{i}")
        time.sleep(0.1)
        # print("RESULT:", result)
        a = ast.literal_eval(result).get("a")
        total += a
    et = time.time()
    print("耗时:", et - st)
    return total


if __name__ == '__main__':
    set_data()
    total = get_data()
    print("total:", total)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis


def get_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    a = {"te": "sfds"}
    str.set("test1", a)
    # print("RESULT:", result)


if __name__ == '__main__':
    get_data()

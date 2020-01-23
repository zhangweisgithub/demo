# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis


def get_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=5, password="ODhzdElWQTIwMTc=")
    print(str)
    a = {"te": "sfds"}
    str.set("token:test1", a)
    str.expire("token:test1", 20)


if __name__ == '__main__':
    get_data()

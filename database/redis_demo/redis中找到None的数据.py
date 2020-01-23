# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis


def get_data():
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    result = str.keys()
    for item in result:
        value = str.get(item)
        # print(value)
        if value.lower() == "none":
            print(item)
            print(value)
    # print("RESULT:", result)


if __name__ == '__main__':
    get_data()

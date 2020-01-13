# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
def get_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    # str = redis.StrictRedis(host="172.20.25.197", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    result = str.keys()
    for item in result:
        # print(item)
        value = str.get(item)
        # print(value)
        if value.lower() == "none":
            print(item)
            print(value)
    # print("RESULT:", result)


if __name__ == '__main__':
    get_data()
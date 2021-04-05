# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import time
import ast

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


import asyncio


async def main():
    print("hello ...")
    await asyncio.sleep(1)
    print("... world")


asyncio.run(main())
if __name__ == '__main__':
    # set_data()
    total = get_data()
    print(total)








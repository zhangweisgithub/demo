# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据准备见: 测试redis连接文件

异步获取redis中对应的数据信息
"""
import redis
import random
import json
import time
import ast
import asyncio
import concurrent.futures


async def factorial(str, i):
    result = str.get(f"set_{i}")
    await asyncio.sleep(0.1)
    # print("RESULT:", result)
    a = ast.literal_eval(result).get("a")
    return a, 1212


if __name__ == '__main__':
    start_time = time.time()
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()
    str = redis.StrictRedis(host="127.0.0.1", port=6379, decode_responses=True, db=1, password="ODhzdElWQTIwMTc=")
    total = 0
    group = []
    st = time.time()
    for i in range(10):
        group.append(factorial(str, i))
    a = loop.run_until_complete(asyncio.wait(group, return_when=concurrent.futures.FIRST_COMPLETED))
    for item in a[0]:
        result = item.result()
        print("aaaa:", result)
        total += result[0]
    end_time = time.time()
    print("最后的结果:", total)
    print("耗时:", end_time - start_time)

"""
aaaa: (10, 1212)
aaaa: (6, 1212)
aaaa: (1, 1212)
aaaa: (2, 1212)
aaaa: (9, 1212)
aaaa: (8, 1212)
aaaa: (7, 1212)
aaaa: (1, 1212)
aaaa: (5, 1212)
aaaa: (7, 1212)
最后的结果: 56
耗时: 0.10871338844299316

"""

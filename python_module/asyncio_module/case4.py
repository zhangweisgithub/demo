# !/usr/bin/env python
# -*- coding: utf-8 -*-
print("---------------------协程Queue-------------------------")
"""
https://www.cnblogs.com/cwp-bg/p/9590700.html
"""
import asyncio
import time
from asyncio import Queue


# async 关键字定义一个协程
async def target_func1(q: Queue):
    for i in range(100):
        await q.put(i)


async def target_func2(q: Queue):
    for i in range(100):
        x = await q.get()
        print(x)


def run1():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    q = Queue(100)
    task = asyncio.gather(target_func1(q), target_func2(q))
    loop.run_until_complete(task)
    loop.close()
    print("Task Done")


if __name__ == '__main__':
    run1()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
协程
关于协程的高质量文章
https://blog.csdn.net/qq_27825451/article/details/102457248
"""
print("---------------------hello world-----------------------")
import asyncio


async def main():
    print("hello ...")
    await asyncio.sleep(1)
    print("... world")


asyncio.run(main())

print("---------------------示例1:耗时3s-----------------------")
"""
%x 本地相应的日期表示
%X 本地相应的时间表示
"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")  # started at 17:31:53

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

print("--------------------示例2:耗时2s(比之前快1s)------------------------")


async def main():
    task1 = asyncio.create_task(
        say_after(1, "hello")
    )
    task2 = asyncio.create_task(
        say_after(2, "world")
    )
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())








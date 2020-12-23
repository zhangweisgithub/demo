# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
可等待对象
如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。许多 asyncio API 都被设计为接受可等待对象。
可等待 对象有三种主要类型: 协程, 任务 和 Future.
"""

print("---------------------协程-------------------------")
"""
协程函数: 定义形式为 async def 的函数;
协程对象: 调用 协程函数 所返回的对象。
"""
import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()  # 筑巢; 巢居; 嵌套(信息);

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())

print("---------------------任务-------------------------")
"""
任务 被用来设置日程以便 并发 执行协程。
当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，该协程将自动排入日程准备立即运行:
"""

import asyncio


async def nested():
    print("ssss")
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task


asyncio.run(main())

print("---------------------Future 对象-------------------------")

"""
Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
"""

print("---------------------sleep-------------------------")
"""
一、获取事件循环
asyncio.get_running_loop()
返回当前 OS 线程中正在运行的事件循环。
如果没有正在运行的事件循环则会引发 RuntimeError。 此函数只能由协程或回调来调用。
"""
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    print("end_time:", end_time)
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


asyncio.run(display_date())



# !/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import datetime
import random
import aiohttp
import aiofiles

"""
图片的下载功能
"""


async def image_downloader(task_q):
    async with aiohttp.ClientSession() as session:
        while not task_q.empty():
            url = await task_q.get()
            try:
                async with session.get(url, timeout=5) as resp:
                    assert resp.status == 200
                    content = await resp.read()
            except Exception as err:
                print('Error for url {}: {}'.format(url, err))
            else:
                fname = split_fname(url)
                print('{} is ok'.format(fname))
                await save_file(fname, content)


def split_fname(url):
    # do something
    return f'FILENAME_AFTER_PROCESSED{random.randint(0, 100)}.jpg'


async def save_file(fname, content):
    async with aiofiles.open(fname, mode='wb') as f:
        await f.write(content)


async def produce_tasks(task_q):
    with open('./images.txt', 'r') as f:
        for count, image_url in enumerate(f):
            image_url = image_url.strip()
            print("image_url:", image_url)
            # if os.path.isfile(split_fname(image_url)):
            #     continue

            await task_q.put(image_url)


async def run():
    task_q = asyncio.Queue(maxsize=1000)
    task_producer = asyncio.ensure_future(produce_tasks(task_q))
    workers = [asyncio.ensure_future(image_downloader(task_q)) for _ in range(10)]
    try:
        await asyncio.wait(workers + [task_producer])
    except Exception as err:
        print(err.__str__())


def main():
    print('start at', datetime.datetime.utcnow())
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asyncio.ensure_future(run()))
    print('end at', datetime.datetime.utcnow())


if __name__ == '__main__':
    main()

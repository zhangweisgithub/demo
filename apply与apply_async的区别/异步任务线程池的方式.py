# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor


"""flask代码可以考虑使用这种线程池的方式进行代码的优化"""
executor = ThreadPoolExecutor()
app = Flask(__name__)


@app.route('/')
def update_redis():
    executor.submit(do_update)
    executor.submit(do_update2)
    return 'ok'


def do_update():
    time.sleep(3)
    print('start update cache')
    time.sleep(1)
    print("end")


def do_update2():
    time.sleep(3)
    print('我是2')
    time.sleep(1)
    print("end2")


if __name__ == '__main__':
    app.run(debug=True)

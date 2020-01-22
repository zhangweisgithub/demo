# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
直接参考以下实例，采用协程访问三个网站,由于IO操作非常耗时，程序经常会处于等待状态
比如请求多个网页有时候需要等待，gevent可以自动切换协程
遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
也可以改成monkey.patch_socket()   monkey.patch_ssl(),那么请求就变成非阻塞的了
一般打补丁在导包之前使用,不然很容易出错,比如在request之后使用就有可能造成
"""
from gevent import monkey

monkey.patch_all()
import gevent
from urllib import request


def run_task(url):
    print("Visit --> %s" % url)
    try:
        response = request.urlopen(url)
        data = response.read()
        print("%d bytes received from %s." % (len(data), url))
    except Exception:
        print("error")


if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    # 定义协程方法
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    # 添加协程任务，并且启动运行
    gevent.joinall(greenlets)

# 查看运行结果可以发现，三个协程是同时触发的，但是结束顺序不同
# 网页请求的时间不同，故结束顺序不同
# 但是该程序其实只有一个线程


"""
Visit --> https://github.com/
Visit --> https://www.python.org/
Visit --> http://www.cnblogs.com/
48595 bytes received from http://www.cnblogs.com/.
48809 bytes received from https://www.python.org/.
125862 bytes received from https://github.com/.
"""
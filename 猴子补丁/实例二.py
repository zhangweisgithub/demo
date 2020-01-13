# !/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
print(socket.socket)    # <class 'socket.socket'>       monkey patch前

from gevent import monkey
monkey.patch_socket()
print(socket.socket)    # <class 'gevent._socket3.socket'>   monkey patch 后,改变了标准socket库



import select
print(select.select)           # <built-in function select>      monkey patch前(通信模块), select()轮询的阻塞调用


monkey.patch_select()
print(select.select)         # <function select at 0x0000029B3D6216A8>     select()轮询的异步调用











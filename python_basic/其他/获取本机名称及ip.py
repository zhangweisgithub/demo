# !/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# 获取本机计算机名称
hostname = socket.gethostname()
print(hostname)  # PV-X00133303
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)  # 192.168.56.1

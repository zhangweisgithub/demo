# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


# 获取本机ip地址
def host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    print(ip)
    return ip


if __name__ == '__main__':
    host_ip()
    # 10.9.176.243





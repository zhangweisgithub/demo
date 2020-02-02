# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1.引模块
2.创建tcp协议的插口
3.插口链接ip及端口
4.发送数据
5.接收数据
6.关闭套接字
"""
import socket

if __name__ == "__main__":
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # 创建客户端插口
    ip_port = ("127.0.0.1", 1111)          # 指定服务器的ip_port
    tcp_socket.connect(ip_port)    # 建立链接
    print(f"{ip_port}链接成功")
    tcp_socket.send("我是tcp客户端中的内容".encode("utf-8"))
    print("发送成功!")
    tcp_bin = tcp_socket.recv(1024)
    print(f"接收成功:{tcp_bin.decode('utf-8')}")
    tcp_socket.close()
    print("成功关闭")









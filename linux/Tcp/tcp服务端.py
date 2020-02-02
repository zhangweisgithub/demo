# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1.socket创建一个套接字
2.bind绑定ip和端口
3.listen是套接字变为可以被动连接
4.accept等待客户端的连接
5.recv/send接收和发送数据
"""

import socket

if __name__ == "__main__":
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建tcp服务器插口
    ip_port = ("127.0.0.1", 1111)
    tcp_server_socket.bind(ip_port)
    tcp_server_socket.listen(128)        # listen变主动为被动套接字
    service_client_socket, ip_port2 = tcp_server_socket.accept()   # 接收客户端发来的链接请求
    print(f"{ip_port2}已连接")
    data_bin = service_client_socket.recv(1024)
    print(ip_port2, data_bin.decode("utf-8"))
    service_client_socket.send("我是tcp服务器的数据".encode("utf-8"))
    service_client_socket.close()
    tcp_server_socket.close()






















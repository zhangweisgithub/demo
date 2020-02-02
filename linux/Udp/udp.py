# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


def send_msg(udp_socket, ip_port):
    str2 = input("请输入想要发送的内容:")
    udp_socket.sendto(str2.encode(), ip_port)
    print("发送成功")


def recv_msg(udp_socket):
    data_bin, ip_port2 = udp_socket.recvfrom(1024)
    print(ip_port2, data_bin.decode("gbk"))


def main():
    # 1.创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.输入IP及端口   (对方的IP地址及端口号)
    IP = input("请输入IP:")
    port = int(input("请输入端口号:"))
    ip_port = (IP, port)
    # 3.死循环进入数据的发送和接收
    while True:
        str1 = input("请输入数值:1.发送  2.退出")
        if str1 == "1":
            # 发送数据
            send_msg(udp_socket, ip_port)
        elif str1 == "2":
            break
        else:
            print("没有此功能")
            continue
        # 发送完毕要接收数据
        recv_msg(udp_socket)

    udp_socket.close()


if __name__ == '__main__':
    main()
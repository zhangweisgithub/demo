# !/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
import paramiko

host = "10.9.242.41"
port = 22
timeout = 30
user = "root"
password = "88stIVA#2019"


def sftp_exec_command(command):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #  # 通过公共方式进行认证 (不需要在known_hosts 文件中存在)
        ssh_client.connect(host, 22, user, password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        for line in std_out:
            print(line.strip("\n"))
        ssh_client.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sftp_exec_command("ls -l & pwd")

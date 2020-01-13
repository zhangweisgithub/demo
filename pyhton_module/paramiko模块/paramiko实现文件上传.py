# !/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko

host = "10.9.242.41"
port = 22
timeout = 30
user = "root"
password = "88stIVA#2019"


def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
        print("文件上传成功!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sftp_upload_file("/docker/paramiko.txt", "D:/paramiko/requirements.txt")

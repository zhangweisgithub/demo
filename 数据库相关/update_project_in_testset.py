# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

#
# def main():
#     conn = pymysql.connect(host="10.9.177.6", user="root", password="88stIVA2017", port=3306, database="web", charset="utf8")
#     cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     print(cs)
#     print(conn)
#     sql_one = "select id,project_id from version"
#     cs.execute(sql_one)
#
#     # project_version = cs.fetchall()
#     # sql_two = "select version_id, project_id from testset"
#     # cs.execute(sql_two)
#     # test_set = cs.fetchall()
#     # for m in test_set:
#     #     for n in project_version:
#     #         if m["version_id"] == n["id"]:
#     #             # m["project_id"] = n["project_id"]
#     #             sql_three = "update testset set project_id = %s where version_id = %s" % (n['project_id'], m['version_id'])
#     #             cs.execute(sql_three)
#     # conn.commit()
#     cs.close()
#     conn.close()
#
#
# if __name__ == '__main__':
#     main()


import socket

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)





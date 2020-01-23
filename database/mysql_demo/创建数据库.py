# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


def main():
    conn = pymysql.connect(host="172.20.25.198", user="root", password="88stIVA2017", port=3306, charset="utf8")
    cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(cs)
    sql_one = "create database functional"
    cs.execute(sql_one)
    hah = cs.fetchall()
    print(hah)
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()

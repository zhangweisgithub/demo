# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import text


def main():
    conn = pymysql.connect(host="10.9.242.41", user="root", password="88stIVA2017", port=3306, database="web", charset="utf8")
    cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(cs)
    sql_one = "select * from %s where id = %s"
    name = "testset"
    num = 390
    param = (name, num)
    cs.execute(text(sql_one), param)
    hah = cs.fetchall()
    print(hah)
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()








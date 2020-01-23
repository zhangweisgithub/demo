# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import text


def main():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="88stIVA2017", database="areas", port=3306,
                           charset="utf8")
    cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(cs)
    # 查找郑州的所有
    sql_one = 'insert into areas values("410101", "中原区", "410100")'
    cs.execute(sql_one)
    conn.commit()  # 这个地方需要进行提交
    hah = cs.fetchall()
    print(hah)
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()

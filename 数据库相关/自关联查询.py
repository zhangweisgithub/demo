# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import text


def main():
    # conn = pymysql.connect(host="10.9.97.8", user="root", password="88stIVA2017", port=3306, database="web", charset="utf8")
    # cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # sql_one = "update testset set is_delete = 0 "
    # sql_one = "select version_id from testset where id = 390"
    # cs.execute(sql_one)
    # conn.commit()
    # cs.close()
    # conn.close()
    conn = pymysql.connect(host="127.0.0.1", user="root", password="88stIVA2017", database="areas", port=3306, charset="utf8")
    cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(cs)
    # 查找郑州的所有
    sql_one = "select * from areas as c join areas as a on a.pid=c.aid where c.atitle='郑州市';"
    cs.execute(sql_one)
    hah = cs.fetchall()
    print(hah)
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
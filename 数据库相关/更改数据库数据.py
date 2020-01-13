# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import text
import datetime


def main():
    # conn = pymysql.connect(host="10.9.97.8", user="root", password="88stIVA2017", port=3306, database="web", charset="utf8")
    # cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # sql_one = "update testset set is_delete = 0 "
    # sql_one = "select version_id from testset where id = 390"
    # cs.execute(sql_one)
    # conn.commit()
    # cs.close()
    # conn.close()
    conn = pymysql.connect(host="127.0.0.1", user="root", password="88stIVA2017", database="web", port=3306,
                           charset="utf8")
    cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    print(cs)
    # 查找郑州的所有
    sql_one = 'UPDATE collection SET updated_time="%s", status=%s WHERE collection.id =%s' % (
    datetime.datetime(2019, 12, 5, 14, 18, 9, 338149), 1, 708)
    # [parameters: {'updated_time': datetime.datetime(2019, 12, 4, 14, 18, 9, 338149), 'status': 3, 'collection_id': 950}]
    cs.execute(sql_one)
    conn.commit()
    hah = cs.fetchall()
    print(hah)
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()

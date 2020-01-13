# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import text, create_engine, MetaData, Table, select


def main():
    engine = create_engine("mysql+pymysql://root:88stIVA2017@127.0.0.1:3306/web?charset=utf8&autocommit=true")
    metadata = MetaData(bind=engine)
    test = Table('case_type', metadata, autoload=True)

    with engine.connect() as connection:
        # Select all from pending_data
        sel = select([test])
        res = connection.execute(sel)

        # do an insert into pending_data
        connection.execute(test.insert().values(type_name='ceshi'))


if __name__ == '__main__':
    main()








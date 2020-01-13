# -*- coding: utf-8 -*-
# @Time    : 2018-05-08 20:14
# @Email   : Yzh_smlie@163.com
# @File    : 数据mysql库操作.py

'''
数据表student有id,name,score,city字段，其中name中的名字可有重复，
需要消除重复行,请写sql语句
select  distinct  name  from  student
'''
'''
show databases;
show tables;
desc 表名;
select * from 表名;
delete from 表名 where id=5;
update students set gender=0,hometown="北京" where id=5
'''

'''
列出常见MYSQL数据存储引擎
    InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），
要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，
也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 
    MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，
那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用。
    MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，
对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在
相对较小的数据库表。
'''

'''sql注入问题：
    以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行
    通过传参数方式解决SQL注入
'''

'''
1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高
级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM
就不可以了；
2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到
安全性较高的应用；
3、InnoDB 支持外键，MyISAM 不支持；
4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM
表中可以和其他字段一起建立联合索引；
5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重
建表；
'''
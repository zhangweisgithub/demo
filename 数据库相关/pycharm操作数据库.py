# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import redis
#
#
# def add_data():
#     str = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
#     result = str.set("name","zhangwei_vendor")
#     print(result)
#
#
# def get_data():
#     str = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
#     result = str.get("a1")
#     print(result)
#
#
# if __name__ == '__main__':
#     get_data()
import redis


# 往redis的数据库里面添加一个数据


def add_data():
    # StrictRedis:固定的语法,初始化redis的对象
    # 第三个参数表示解码,在redis里面进行操作数据的时候,都是通过byte数据操作,获取的时候,如果需要改成string类型,所以必须进行解码
    str = redis.StrictRedis(host="localhost", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print("name:", str.__getitem__())
    # # 如果redis的数据设置成功,会返回一个ture
    print(str)
    result = str.set("age", "27")
    print(result)
    # str = redis.StrictRedis(host="10.9.97.8", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    # key = "test123"
    # process = {"process": 0.000, "test": "121"}
    # str.set(key, "%s" % process)
    # redis_key_get = "collection_%s_set_%s" % (1, 12)
    # str.set(redis_key_get, "%s" % process)


def get_data():
    # str = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    str = redis.StrictRedis(host="10.9.244.33", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    # result = str.get("collection_4_set_1209")
    result = str.get("set_1282")
    # re = json.dumps(result)
    # re = eval(result)
    # print(type(eval(result)))
    print("RESULT:", result)

def get_ubunut_data():
    str = redis.StrictRedis(host="192.168.117.3", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    print(str)
    result = str.get("set_1523")
    print("RESULT:", result)

if __name__ == '__main__':
    # add_data()
    # get_data()
    get_ubunut_data()

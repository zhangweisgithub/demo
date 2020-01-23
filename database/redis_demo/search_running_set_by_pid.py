# !/usr/bin/env python
# -*- coding: utf-8 -*-
import redis


# 根据进程号查询正在运行的测试集
def get_data():
    # conn = redis.StrictRedis(host="192.168.117.5", port=6379, decode_responses=True)
    conn = redis.StrictRedis(host="172.20.25.197", port=6379, decode_responses=True, db=0, password="ODhzdElWQTIwMTc=")
    data = input("请输入pid:")
    keys = conn.keys()
    result = []
    for key in keys:
        value = conn.get(key)
        try:
            if type(eval(str(value))) != dict:
                continue
        except:
            continue
        if data == eval(value).get("pid") and eval(value).get("status") == 2:
            result.append(key)
    if not result:
        print("无测试集运行在%s进程中" % data)
    else:
        print("测试集 %s正运行在%s进程中" % (result, data))


if __name__ == '__main__':
    get_data()

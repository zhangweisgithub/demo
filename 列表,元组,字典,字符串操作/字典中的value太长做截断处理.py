# !/usr/bin/env python
# -*- coding: utf-8 -*-
import time
a = {"hah": {u"task_id": u"Traceback (most recasfasdfasfas)"}, 'case_50114': 'failasfas', 'pass_num': 3, 'total_num': 9, 'case_50108': 'passasfdf', 'case_50110': 'pass', 'case_50111': 'fail', 'case_50112': 'fail', 'progress': 0.667, 'fail_num': 3, 'case_50109': 'pass'}
# # a = a.decode("utf-8")
# # print(type(a))
# print(type(eval(a)))


import sys
string_types = str if sys.version_info[0] == 3 else basestring
# print(string_types)


def keys_ignore_value(input_json, length=500,
                      ignore_key=["title", "reason", "url", "expect", "detail", "http_request", "log"]):
    """
    的递归获取key对应的value
    :param input_json:
    :param length:
    :param ignore_key:
    :return:
    """
    if isinstance(input_json, dict):
        for key, json_result in input_json.items():
            if key in ignore_key:
                pass
            else:
                if isinstance(json_result, string_types):
                    if "Traceback" in json_result:
                        print("1", length)
                        print("3:", len(json_result))
                        pass
                    elif "HTTPConnectionPool" in json_result:
                        pass
                    elif len(json_result) > length:
                        input_json[key] = json_result[0:19] + "..."
                        print("2")
                    else:
                        pass
                else:
                    keys_ignore_value(json_result, length)
    elif isinstance(input_json, list):
        for json_array in input_json:
            keys_ignore_value(json_array, length)
    elif isinstance(input_json, string_types):
        return input_json
    return input_json


# print(keys_ignore_value(a, 666))
print(len(str(b)))
steps=str(keys_ignore_value(b, 5)) if len(str(b)) > 1000 else str(b),
print(steps)

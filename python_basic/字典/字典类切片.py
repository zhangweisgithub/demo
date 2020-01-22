# !/usr/bin/env python
# -*- coding: utf-8 -*-


a = {"a": {"a": "b"}, "b": "c", "d": "e", "f": "asfdsa", "g": "asfdasfaw", "h": "asfdsa2w", "i": "asfwere"}


def dict_slice(ori_dict, length):
    len_dict = len(str(ori_dict))
    if isinstance(ori_dict, dict):
        while len_dict > length:
            if len(ori_dict.keys()) > 1:
                ori_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[0: -1]}
                print(ori_dict)
                len_dict = len(str(ori_dict))
    elif isinstance(ori_dict, list):
        for json_array in ori_dict:
            dict_slice(json_array, length)
    elif isinstance(ori_dict, str):
        return ori_dict
    return ori_dict


b = dict_slice(a, 50)
print("结果:", b)

print("----------------我是分割线---------------------")


def dict_slice2(ori_dict, start, end):
    """
    字典类切片
    :param ori_dict: 字典
    :param start: 起始
    :param end: 终点
    :return:
    """
    slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
    return slice_dict


print(dict_slice2(a, 1, -1))

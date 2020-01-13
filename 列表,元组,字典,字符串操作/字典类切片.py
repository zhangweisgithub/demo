# !/usr/bin/env python
# -*- coding: utf-8 -*-


# def dict_slice(ori_dict, start, end):
#     slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
#     return slice_dict


a = [{"a": {"a": "b"}, "b": "c", "d": "e", "f": "asfdsa", "g": "asfdasfaw", "h": "asfdsa2w", "i": "asfwere"}]
# print(len(a.keys()))
# print(dict_slice(a, 0, -1))

# import pysnooper
# @pysnooper.snoop()
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


dict_slice(a,50)



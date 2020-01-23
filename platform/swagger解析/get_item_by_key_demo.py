# !/usr/bin/env python
# -*- coding: utf-8 -*-


def get_item_by_key(obj, key, result=None):
    if isinstance(obj, dict):
        for k in obj:
            if key == k:
                if isinstance(result, list):
                    if isinstance(obj[k], list):
                        result.extend(obj[k])  # 如果value是一个列表,extend到result列表中['test2', 'test1']
                    else:
                        result.append(obj[k])  # 如果value不是列表,append到result列表中['test2', 'test1']
                elif result is None:
                    result = obj[k]  # 如果result为空,结果为value值
                else:
                    result = [result, obj[k]]  # 否者,将得到的结果添加到后面: [{'test2': 'asfd'}, 'test1']
            else:
                if isinstance(obj[k], dict) or isinstance(obj[k], list):  # 如果value是字典或列表的嵌套,继续调用自己
                    result = get_item_by_key(obj[k], key, result)  # result继承之前获取到的数据
    elif isinstance(obj, list):
        for i in obj:
            if isinstance(i, dict) or isinstance(i, list):
                result = get_item_by_key(i, key, result)
    return result[0] if isinstance(result, list) and len(result) == 1 else result  # 如果结果是一个列表而且只有一个数据,就返回数据本身


if __name__ == '__main__':
    a = [{"test": "test1"}]
    res = get_item_by_key(a, "test", {'test2': 'asfd'})
    print(res)  # [{'test2': 'asfd'}, 'test1']

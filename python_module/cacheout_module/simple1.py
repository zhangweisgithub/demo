# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
特性：

后端使用字典进行缓存

使用缓存管理轻松访问多个缓存对象

当使用模块级缓存对象，重构运行时的缓存设置

最大缓存大小限制

默认的缓存时间设置以及缓存项自定义存活时间

批量的设置、获取、删除操作

线程安全

多种缓存机制的实现：

FIFO(先进先出)

LIFO(后进先出)

LRU (最近最少使用机制)

MRU (最近最多使用机制)

LFU (最小频率使用机制)

RR (随机替换机制)

解释一下，避免产生混淆，我在使用时就产生的歧义，后来通过小demo证实的!

LRU是删除最近最少使用的，保留最近最多使用的。

线路图：

层级缓存(多层级缓存)

支持缓存事件监听

获取缓存对象时的常规表示方法

获取缓存对象不存在时的回调处理支持

统计缓存
"""
# from cacheout import Cache# 如果选择LFUCache 就导入即可
# from cacheout import LFUCache
# cache = LFUCache()
import time
from cacheout import Cache

# 默认的缓存大小为256, 默认存活时间是关闭的
cache = Cache(maxsize=256, ttl=0, timer=time.time, default=None)

# 通过key/value的形式进行set与get
cache.set(1, 'foobar')
cache.set(2, 'foobar2')
ret = cache.get(1)
print("ret:", ret)

# 可以为每个键值对设置存活过期时间:
# cache.set(3, {"data": {}}, ttl=1)
# assert cache.get(3) == {"data": {}}
# time.sleep(2)
# assert cache.get(3) == {"data": {}}

# 为缓存函数提供了键值对的存活时间：
# @cache.memoize()
# def func(a, b):
#     pass
#
#
# @cache.memoize()
# def func(a, b):
#     pass
#
#
# # 函数解除缓存：
# func.uncached(1, 2)

# 复制机制
# assert cache.copy() == {1: 'foobar', 2: ('foo', 'bar', 'baz')}

# 删除缓存中的一个键值对
cache.delete(1)
assert cache.get(1) is None

# 清除整个缓存
print(len(cache))
cache.clear()
assert len(cache) == 0

# 为get, set, delete设置了批量方法
cache.set_many({"a": 1, "b": 2, "c": 3})
assert cache.get_many(["a", "b", "c"])
print(len(cache))
assert cache.delete_many(["a", "b", "c"])
print(len(cache))

# 重置已经初始化的缓存对象
cache.configure(maxsize=1000, ttl=5*60)
cache.set_many({'a': 1, 'b': 2, 'c': 3})
assert list(cache.keys()) == ['a', 'b', 'c']
assert list(cache.values()) == [1, 2, 3]
assert list(cache.items()) == [('a', 1), ('b', 2), ('c', 3)]

# 迭代整个缓存的key
for key in cache:
    print(key, cache.get(key))
    # 'a' 1
    # 'b' 2
    # 'c' 3

assert cache.has('a')
assert 'a' in cache
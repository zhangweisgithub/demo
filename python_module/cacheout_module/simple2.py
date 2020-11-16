# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TTL是 Time To Live的缩写，该字段指定IP包被路由器丢弃之前允许通过的最大网段数量
1、建立在内存上，其处理速度优于redis，等同于内存
2、可以设置过期时间，以及缓存容量大小，控制占用内存的大小
3、可以选择适合自己的机制，进一步优化优先策略，优于内存
"""

from cacheout import CacheManager, LFUCache

# 设置多个缓存， 并设置缓存机制
cacheman = CacheManager({'a': {'maxsize': 100},
                         'b': {'maxsize': 200, 'ttl': 900},
                         'c': {}},
                        cache_class=LFUCache
                        )

cacheman['a'].set('key1', 'value1')
value = cacheman['a'].get('key1')
print("value:", value)

cacheman['b'].set('key2', 'value2')
assert cacheman['b'].maxsize == 200
assert cacheman['b'].ttl == 900

cacheman['c'].set('key3', 'value3')

cacheman.clear_all()
for name, cache in cacheman:
    assert name in cacheman
    assert len(cache) == 0

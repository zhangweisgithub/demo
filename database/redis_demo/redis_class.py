# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import redis


class Error(Exception):
    """Base class for exceptions."""

    code = 3
    msg = "Error"

    def __str__(self):
        return json.dumps({"code": self.code, "msg": self.msg}, ensure_ascii=False)


class PerfError(Error):
    """Exception raised for errors in internal code

    Attributes:
        message - - explanation of the error
    """
    def __init__(self, code=3, msg="perf服务异常"):
        self.code = code
        self.msg = msg


class RedisBase:
    def __init__(self, key, timeout=0) -> None:
        print("base_key:", key)
        redis_url = "redis://:ODhzdElWQTIwMTc=@127.0.0.1:6379/3"
        self._redis_store = redis.StrictRedis.from_url(redis_url, decode_responses=True)
        self._key = key
        self._timeout = timeout

    def _getv(self, value):
        if value is None:
            return value
        else:
            return json.loads(value)

    def _setv(self, value):
        # 类型检查
        allow_types = (str, int, float, bool, dict, list, tuple)
        if not isinstance(value, allow_types):
            raise PerfError(msg=f'值类型错误:{value}:{type(value)}, 仅支持{allow_types}')
        return json.dumps(value)

    def _getk(self, key):
        return json.loads(key)

    def _setk(self, key):
        # 类型检查
        allow_types = (str, int, float, bool)
        if not isinstance(key, allow_types):
            raise PerfError(msg=f'键类型错误:{key}:{type(key)}, 仅支持{allow_types}')
        return json.dumps(key)

    def clear(self):
        print("清除:", self._key)
        self._redis_store.delete(self._key)

    def __repr__(self) -> str:
        """
        __repr__() 方法是类的实例化对象用来做“自我介绍”的方法，默认情况下，它会返回当前对象的“类名+object at+内存地址”，
        而如果对该方法进行重写，可以为其制作自定义的自我描述信息。
        :return:
        """
        return repr(self._all)

    def __str__(self) -> str:
        """
        当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
        __str__方法需要返回一个字符串，当做这个对象的描写
        :return:
        """
        return str(self._all)

    def __iter__(self):
        """
        @summary: 迭代器，生成迭代对象时调用，返回值必须是对象自己,然后for可以循环调用next方法
        :return:
        """
        return iter(self._all)


class RedisDict(RedisBase):
    # 实现一个存储在redis的类似字典的类型，数据每次读写都是操作redis上的数据，使用时需要考虑并发操作问题
    def __init__(self, key: str, data: dict = None, timeout=0):
        super(__class__, self).__init__(key, timeout)
        print("11111:", key, data)
        if data is not None:
            self.clear()
            self.update(data)

    @property
    def _all(self) -> dict:
        """
        我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,
        可以与所定义的属性配合使用，这样可以防止属性被修改。
        Redis Hgetall 命令用于返回哈希表中，所有的字段和值
        :return:
        """
        all = self._redis_store.hgetall(self._key)
        return {self._getk(k): self._getv(v) for k, v in all.items()}

    def __len__(self):
        """
        Returns the length of a hash, in number of items
        :return:
        """
        return self._redis_store.hlen(self._key)

    def __setitem__(self, key, value):
        if value is None:
            return
        self._redis_store.hset(self._key, self._setk(key), self._setv(value))
        if self._timeout:
            self._redis_store.expire(self._key, self._timeout)

    def __getitem__(self, key):
        value = self._redis_store.hget(self._key, self._setk(key))
        return self._getv(value)

    def __delitem__(self, key):
        # TODO:考虑key不存在的情况
        return self._redis_store.hdel(self._key, self._setk(key))

    def __contains__(self, key):
        return self._redis_store.hexists(self._key, self._setk(key))

    def get(self, key, default=None):

        if self._redis_store.hexists(self._key, self._setk(key)):
            return self.__getitem__(key)
        else:
            return default

    def pop(self, key):
        pip = self._redis_store.pipeline(True)
        pip.watch(self._key)
        pip.multi()
        ret = pip.hget(self._key, self._setk(key))
        pip.hdel(self._key, self._setk(key))
        pip.execute()
        return ret

    def items(self):
        return self._all.items()

    def keys(self):
        return self._all.keys()

    def values(self):
        return self._all.values()

    def update(self, data: dict):
        tmp = {self._setk(k): self._setv(v) for k, v in data.items() if v is not None}
        print("tmp:", tmp)
        if tmp:
            # Redis Hmset 命令用于同时将多个 field-value (字段-值)对设置到哈希表中
            self._redis_store.hmset(self._key, tmp)
            if self._timeout:
                self._redis_store.expire(self._key, self._timeout)

    def todict(self):
        return self._all


class RedisList(RedisBase):
    # 实现一个存储在redis的类似列表的类型，数据每次读写都是操作redis上的数据，使用时需要考虑并发操作问题
    def __init__(self, key: str, data: list = None):
        super(__class__, self).__init__(key)
        if data is not None:
            self.clear()
            data = [self._setv(x) for x in data]
            self._redis_store.rpush(self._key, *data)

    @property
    def _all(self) -> list:
        all = self._redis_store.lrange(self._key, 0, -1)
        return [self._getv(x) for x in all]

    def __len__(self):
        return self._redis_store.llen(self._key)

    def __setitem__(self, index, value):
        self._redis_store.lset(self._key, index, self._setv(value))

    def __getitem__(self, index):
        value = self._redis_store.lindex(self._key, index)
        return self._getv(value)

    def __delitem__(self, index):
        """删除指定位置的元素"""
        raise PerfError(msg='暂不支持按序号删除元素')

    def __contains__(self, value):
        return value in self._all

    def append(self, value):
        self._redis_store.rpush(self._key, self._setv(value))

    def remove(self, value):
        self._redis_store.lrem(self._key, 1, self._setv(value))

    def tolist(self):
        return self._all


if __name__ == "__main__":
    # 新建空对象
    task_pool = RedisDict('TASK_POOL', {})
    print(f'新建空对象:{task_pool}')
    # 新建对象
    task_pool = RedisDict('TASK_POOL', {'this': 111})
    print(f'新建对象:{task_pool}')
    # 更新字段
    task_pool['case_123'] = 'helloworld'
    print(f'更新字段:{task_pool}')
    # 批量更新字段
    task_pool.update({'aaa': 111, 'bbb': 222})
    print(f'批量更新字段:{task_pool}')
    print("哈希表中字段的数量:", task_pool.__len__())
    # 读取对象
    task_pool = RedisDict('TASK_POOL')
    print(f'读取对象:{task_pool}')       # 返回RedisBase基类中定义的__str__方法的返回值
    # # 删除字段
    del task_pool['case_123']
    print(f'删除字段:{task_pool}')
    # 包含对象
    print(f'"case_123" in task_pool:{"case_123" in task_pool}')
    # 字段数量
    print(f'len(task_pool):{len(task_pool)}')   # task_pool的类型:<class '__main__.RedisDict'>
    # 替换对象
    task_pool = RedisDict('TASK_POOL', {'other': 123})
    print(f'替换对象:{task_pool}')
    # 替换成空对象
    task_pool = RedisDict('TASK_POOL', {})
    print(f'替换成空对象:{task_pool}')
    # 删除对象
    task_pool.clear()
    print(f'删除对象:{task_pool}')

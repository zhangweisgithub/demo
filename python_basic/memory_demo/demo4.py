# !/usr/bin/env python
# -*- coding: utf-8 -*-
import wrapcache
from time import sleep
import random


@wrapcache.wrapcache(timeout=3)
def need_cache_function(input, t=2, o=3):
    sleep(2)
    return random.randint(1, 100)


if __name__ == "__main__":
    for i in range(10):
        # sleep(1)
        print(need_cache_function(1, t=2, o=3))

    # get cache Programmatic
    key_func = wrapcache.keyof(need_cache_function)
    print(wrapcache.get(key_func))

    # remove cache Programmatic
    # print(wrapcache.remove(wrapcache.keyof(need_cache_function, 1, o=3, t=2)))

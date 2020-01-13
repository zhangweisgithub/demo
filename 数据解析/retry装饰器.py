# !/usr/bin/env python
# -*- coding: utf-8 -*-


def retry(MAXRETRY=3):
    def decorator(func):
        def wrapped(*args, **kwargs):
            print("进入装饰器")
            result = 0
            retry = 1
            while result != 200 and retry <= MAXRETRY:
                result = func(*args, **kwargs)
                print("重试第%s次" % retry)
                print("结果:", result)
                retry += 1
            return result

        return wrapped

    return decorator


@retry(5)
def request_page():
    print("访问一个网页")
    print("得到了response")
    return 400


if __name__ == '__main__':
    request_page()

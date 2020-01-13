# !/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


if __name__ == '__main__':
    a = convert_path(os.path.dirname(__file__))
    print(a)


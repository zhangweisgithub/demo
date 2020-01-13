# !/usr/bin/env python
# -*- coding: utf-8 -*-
f = {"code": 0}
a = {}
def main():
    a.setdefault(None, []).append(f)
    print(a)


main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

pytest.main()  # 基本用法
pytest.main(['-x', 'mytestdir'])  # 传入配置参数

# // 指定自定义的或额外的插件
# content of myinvoke.py
import pytest


class MyPlugin(object):
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


pytest.main(["-qq"], plugins=[MyPlugin()])

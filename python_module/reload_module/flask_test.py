# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""imp 从 Python 3.4 之后弃用了，建议使用 importlib 代替"""
from flask import Flask
from python_module.reload_module import func_test
import importlib
app = Flask(__name__)


@app.route('/')
def test():
    importlib.reload(func_test)          # 对模块进行动态加载
    data = func_test.func1()
    return str(data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5553)



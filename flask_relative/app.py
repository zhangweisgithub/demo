# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello"


if __name__ == '__main__':
    print('dd', __name__)    # 如果直接执行此文件__name__==__main__
    app.run(host="127.0.0.1", port=1235)

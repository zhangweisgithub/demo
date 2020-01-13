# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.debug = True
    app.run()


"""
gunicorn的作用就是用命令来启动服务器: gunicorn main:app
"""


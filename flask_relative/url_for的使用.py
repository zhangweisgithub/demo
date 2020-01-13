#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: cxa
@file: flask03.py
@time: 2018/04/13 15:20
"""
"""url_for的用法
本质是根据函数名反向生成url，使用函数 url_for() 来针对一个特定的函数构建一个 URL。
它能够接受函数名作为第一参数，以及一些关键字参数， 每一个关键字参数对应于 URL 规则的变量部分。未知变量部分被插入到 URL 中作为查询参数。
url_for()还可以用来构造url，就比如说，url('static',filename='1.png')，代表我访问static/1.png就可以直接访问到这张图片，还是很有用的这个函数。
"""
from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def Index():
    return "<h1>this is Index Page</h1>"


@app.route('/test')
def query_user():
    """
      http://127.0.0.1:5000/test?id=123
    :return:
    """
    id = request.args.get('id')
    return "query user:" + id


@app.route('/query_url')
def query_url():
    """
    反导向query_user函数名对应的url地址
    :return
    """
    return "query url:" + url_for("query_user")


if __name__ == "__main__":
    app.run(debug=True)

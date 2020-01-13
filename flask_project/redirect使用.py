# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for, render_template, Response, jsonify, make_response

app = Flask(__name__)


@app.route('/a')
def a():
    return redirect(url_for('ccc222'))  # url_for直接对函数访问


@app.route('/b')
def b():
    return redirect("http://127.0.0.1:5000/ccc111")  # redirect直接对route的路径访问


@app.route('/ccc111')
def ccc222():
    return "我是ccc"


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()



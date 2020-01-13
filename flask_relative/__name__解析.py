# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<id>')
def hello_world(id):
    return json.dumps({'Hello World!': id}, ensure_ascii=False)  # 返回给前端的数据本质上是字符串


@app.route('/hello')
def hello_world2():
    wordd = "你好"
    return hello_world(123)  # 返回给前端的数据本质上是字符串


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9006, debug=True)

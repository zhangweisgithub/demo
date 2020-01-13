# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import Response
import json

"""jsonify与json.dumps都可以把字典转化为json数据格式的,但是,返回的类型是不同的
    jsonify返回的是application/json类型的数据,json.dumps(ensure_ascii=False),返回的content_type:txt/html
"""
app = Flask(__name__)


@app.route('/hello/<name>/<words>',methods=["GET"])
def hello(name,words):
    return json.dumps({"name":name,"words":words},ensure_ascii=False)


if __name__=='__main__':
    app.run()


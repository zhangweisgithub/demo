# !/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta
from io import BytesIO
from flask import make_response, Flask, session, jsonify
from python_module.pillow_module.application.urls import validate_picture
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)  # 生成24位随机数

"""
在flask项目中，Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，这是一个比较重要的配置值。
在使用flask时，我产生了这个错误：the session is unavailable because no secret key was set. 
Set the secret_key on the application to something unique and secret
解决方法是在flask项目开头加入设置SECRET_KEY。
"""


@app.route('/')
def get_code():
    image, str1 = validate_picture()
    # 讲验证码图片以二进制形式写入内存，防止图片都放在文件夹中，占用磁盘空间
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置头部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 验证码字符串存储在seesion中
    session['image'] = str1
    print("获取image:", session.get("image"))
    session.permanent = True  # 设置session永久有效  注意这个要设置在request里边 即请求内部
    app.permanent_session_lifetime = timedelta(seconds=10)  # 设置session的有效时间为10s
    return response


@app.route('/session')
def get_session():
    """
    可以通过这个接口查看session的是否在内存职中以及是否有效
    :return:
    """
    image = session.get("image")
    return jsonify({"session": image})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9006, debug=True)

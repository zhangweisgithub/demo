# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = 1 / 1
    return 'Hello World!'


# 当设置debug=True的时候,当我们更新代码的时候,项目会自动重新reloading
# 在debug模式下使用user_reload=False参数时,项目不会再重新启动
# 如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1568, debug=False)

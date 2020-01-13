# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


"""
解释：
即使传递其他参数，最终也只会读取定义的2个参数的值
通过如上代码说明：reqparse.RequestParser.parse_args()，即如上的args可以获取到request的form表单的参数，最终是一个字典
"""
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('name', type=str)


# 获取  &  更新
class Get_Modify(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        return args, 201


api.add_resource(Get_Modify, '/get_modify')

if __name__ == '__main__':
    app.run(debug=True)



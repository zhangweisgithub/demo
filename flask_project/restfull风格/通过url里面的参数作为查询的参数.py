# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

Tasks = {
    't1': {'task': 'eat an app'},
    't2': {'task': 'play football'},
    't3': {'task': 'watching TV'},
}


def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Tasks:
        abort(404, message="Todo {} doesn't exist".format(t_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# 更新 & 删除  任务
class Updata_Delete(Resource):
    def get(self, t_id):               # 根据t_id获取对应的value
        abort_if_todo_doesnt_exist(t_id)
        return Tasks[t_id]

    def delete(self, t_id):            # 根据t_id删除对应的value
        abort_if_todo_doesnt_exist(t_id)
        del Tasks[t_id]
        return '{delete success}'

    def post(self, t_id):            # 判断t_id是否存在，并返回Tasks整个列表
        abort_if_todo_doesnt_exist(t_id)
        return Tasks,201

    def put(self, t_id):            # 根据t_id添加对应的value，并返回所有值
        args = parser.parse_args()
        task = {'task': args['task']}
        Tasks[t_id] = task
        return Tasks, 201


api.add_resource(Updata_Delete, '/update_delete/<t_id>')

if __name__ == '__main__':
    app.run(debug=True)








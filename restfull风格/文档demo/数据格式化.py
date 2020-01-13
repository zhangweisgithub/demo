# !/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict
from flask.ext.restful import fields, marshal_with
from flask_restful import Resource

resource_fields = {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
}


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

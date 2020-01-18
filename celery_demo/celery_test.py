# !/usr/bin/env python
# -*- coding: utf-8 -*-
from celery import Celery

app = Celery("task",
             broker="redis://:ODhzdElWQTIwMTc=@127.0.0.1",
             backend="redis://:ODhzdElWQTIwMTc=@127.0.0.1", )


@app.task(name="asfda")
def add(x, y):
    print("running...", x, y)
    return x + y


if __name__ == '__main__':
    add.delay(1, 2)

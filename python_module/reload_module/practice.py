# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pkgutil
import sys
import traceback
from flask import Flask, current_app
import json
import importlib
importlib.reload(sys)
import python_module.reload_module.func_test
app = Flask(__name__)


@app.route('/')
def hello_world():
    import python_module.reload_module as modules
    reload_modules(modules, log=current_app.logger)          # 先对函数进行reload操作,然后再调用函数
    data = python_module.reload_module.func_test.func1()
    return json.dumps({"code": str(data)})  # 返回给前端的数据本质上是字符串


def reload_modules(module, log=None, out=[]):
    try:
        importlib.reload(module)
    except:
        pass
    try:
        for loader, name, ispkg in pkgutil.iter_modules(module.__path__, module.__name__ + "."):
            if not ispkg:
                if "gitlab" in name:
                    continue
                new_module = loader.find_module(name).load_module(name)
                if name in list(sys.modules.keys()):
                    try:
                        importlib.reload(sys.modules[name])
                        if log:
                            log.info("reload module: {0}".format(name))
                            print("reload: {0}".format(name))
                        else:
                            print("reload: {0}".format(name))
                    except (ModuleNotFoundError, IndentationError, SyntaxError) as e:
                        if log:
                            log.info(traceback.format_exc())
                        else:
                            print(traceback.format_exc())
                        out.append(traceback.format_exc())
                    finally:
                        pass
                else:
                    sys.modules[name] = new_module
                    if log:
                        log.info("new module: {0} add to sys modules".format(name))
                    else:
                        print("new module: {0} add to sys modules".format(name))
            else:
                new_module = loader.find_module(name).load_module(name)
                reload_modules(new_module, log)
    except:
        if log:
            log.error(traceback.format_exc())
        else:
            out.append(traceback.format_exc())
    return out


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9006)


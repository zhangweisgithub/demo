# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-




# coding=UTF-8
import sys
import importlib
import traceback
import inspect
import base64
import json
import pkgutil
sys.path.append("D:\\platform\\backend-api")
sys.path.append("D:\\platform\\backend-api\\scripts\\vats")
if __name__ == "__main__":
    from common.public import get_func_param_desc, log_handler
    log = log_handler(filename="D:\\platform\\backend-api\\app.log")
    pres = []
    try:
        import viper_pre as modules
    except:
        log.error(traceback.format_exc())
        modules = dict()
        if modules:
            module_list = []
            for loader, name, ispkg in pkgutil.iter_modules(modules.__path__, modules.__name__ + "."):
                module_list.append(importlib.import_module(name))
                for module in module_list:
                    for name, func in inspect.getmembers(module, predicate=inspect.isfunction):
                        description = get_func_param_desc(func.__doc__) if func.__doc__ else ""
                        val = {"name": str.split(module.__name__, ".")[-1] + "." +  name, "args":  description, "type": 2}
                        if val not  in pres:
                            pres.append(val)
                            ret = "Start:"+ str(base64.b64encode(json.dumps(pres).encode("utf-8")), encoding="utf-8") + ":End"
                            sys.stdout.write(ret)










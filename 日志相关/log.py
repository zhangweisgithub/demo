# !/usr/bin/env python
# -*- coding: utf-8 -*-


def initlog():
    import logging
    logger = None
    logger = logging.getLogger()
    hdlr = logging.FileHandler("kws30.log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    # logger.propagate = 0
    return [logger, hdlr]


def logMsg(fun_name, err_msg, level):
    message = fun_name + ':' + err_msg
    logger, hdlr = initlog()
    logger.log(level, message)
    hdlr.flush()

    logger.removeHandler(hdlr)  # 网络上的实现基本为说明这条语句的使用和作用


if (__name__ == "__main__"):
    for k in ["fun1", "fun2", "fun3", "func4"]:
        logMsg("main", k, 1)
        print("1111")
    # logMsg("我", "是",1)
    # try:
    #     1 / 0
    # except Exception as e:
    #     logMsg("main", str(e), 1)

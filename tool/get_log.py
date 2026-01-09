#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/12/26 17:14
# @Author  : songyoukang
# @File    : get_log.py
# @Software: PyCharm
import logging.handlers
import os
from config import BASE_PATH

class GetLog():
    #新建日志变量
    __logger=None
    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器是否为空
        if cls.__logger is None:
            #获取日志器
            cls.__logger=logging.getLogger()
            #修改默认级别
            cls.__logger.setLevel(logging.INFO)
            log_path=BASE_PATH +os.sep + "log" + os.sep + 'zhiwei_auto.log'
            #获取处理器
            th=logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                         when="midnight",
                                                         backupCount=3,
                                                         encoding="utf-8"
                                                         )
            #获取格式器
            fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            #将格式器添加到处理器中
            th.setFormatter(fm)
            #将处理器添加到日志器中
            cls.__logger.addHandler(th)

        #返回日志器
        return  cls.__logger
if __name__ == '__main__':
    re=GetLog.get_logger()
    re.info("测试信息级别日志")
    re.error("测试错误级别日志")
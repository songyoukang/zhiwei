#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 15:00
# @Author  : songyoukang
# @File    : getdriver.py
# @Software: PyCharm
from selenium import webdriver
import page
class DriverUtil():
    """获取浏览器对象"""
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # cls.driver = webdriver.Chrome() #定义chrome浏览器驱动
            cap={
            "browserName":"chrome",
            "version":'',
            "Platform":"WINDOWS"
            }
            cls.driver = webdriver.Remote("http://10.10.10.38:4444/wd/hub",cap)
            cls.driver.get(page.web_url) #定义访问环境地址
            cls.driver.maximize_window() #窗口最大化1
            cls.driver.implicitly_wait(10) #隐式等待10s
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
if __name__ == '__main__':
    DriverUtil.get_driver()

#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 17:27
# @Author  : songyoukang
# @File    : Test_center_login.py
# @Software: PyCharm
import pytest
from page.page_in import Page_in
from base.getdriver import DriverUtil
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
log=GetLog.get_logger()
class Testlogin():
    """业务层"""
    def setup(self):
        #获取driver
        self.driver=DriverUtil.get_driver()
        #获取统一入口类
        self.login=Page_in(self.driver).get_page_center_login()
    def teardown(self):
        DriverUtil.quit_driver()
    @pytest.mark.parametrize("username,passwd", read_yaml("login.yaml"))
    @pytest.mark.run(order=1)
    def testlogin(self, username, passwd):
        try:
            # 调用1次登录方法，接收返回结果
            login_result = self.login.page_center_login(username, passwd)
            # 断言登录成功，失败则触发AssertionError
            assert login_result is True, f"账号【{username}】登录失败！"

            # 登录成功的日志（格式更清晰）
            log.info(f"✅ 账号【{username}】登录成功 → ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        except AssertionError as ae:
            # 单独捕获登录失败的断言异常，日志更精准
            log.info(f"❌ 账号【{username}】登录失败：{ae}")
            raise  # 抛出，让pytest标记用例失败


# if __name__ == '__main__':
#     Testlogin()
#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:44
# @Author  : songyoukang
# @File    : Test_center_createrole.py
# @Software: PyCharm
from tool.get_log import GetLog
log=GetLog.get_logger()
import pytest
from page.page_in import Page_in
from base.getdriver import DriverUtil
class Test_Center_Updaterole():
    """业务层"""
    def setup(self):
        #获取driver
        self.driver=DriverUtil.get_driver()
        #获取统一入口类
        self.page_in=Page_in(self.driver)
        self.page_in.get_page_center_login().page_login_updaterole()
        self.updaterole=self.page_in.get_page_center_updaterole()
    def teardown(self):
        DriverUtil.quit_driver()
    @pytest.mark.run(order=6)
    def test_center_updaterole(self):
        log.info("++++++++++++++++开始执行更新角色操作+++++++++++++++++++++++")
        try:
            # 调用1次登录方法，接收返回结果
            updaterole_result=self.updaterole.page_center_updaterole()
            log.info(f"获取的文本内容为{updaterole_result}")
            # 断言登录成功，失败则触发AssertionError
            assert "自动化测试角色修改" ==  updaterole_result, f"【自动化测试角色修改】修改失败！"
            # 登录成功的日志（格式更清晰）
            log.info(f"✅ 角色【{updaterole_result}】修改成功 → ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except AssertionError as ae:
            # 单独捕获登录失败的断言异常，日志更精准
            log.info(f"❌ 角色【自动化测试角色修改】修改失败：{ae}")
            raise  # 抛出，让pytest标记用例失败

if __name__ == '__main__':
    Test_Center_Updaterole()
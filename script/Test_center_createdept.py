#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:44
# @Author  : songyoukang
# @File    : Test_center_createdept.py
# @Software: PyCharm
from tool.get_log import GetLog
log=GetLog.get_logger()
import pytest
from page.page_in import Page_in
from base.getdriver import DriverUtil
class Test_Center_Createdept():
    """业务层"""
    def setup(self):
        #获取driver
        self.driver=DriverUtil.get_driver()
        #获取统一入口类
        self.page_in=Page_in(self.driver)
        self.page_in.get_page_center_login().page_login_createdept()
        self.createdept=self.page_in.get_page_center_createdept()
    def teardown(self):
        DriverUtil.quit_driver()
    @pytest.mark.run(order=8)
    def test_center_createdept(self):
        log.info("++++++++++++++++开始执行添加部门操作+++++++++++++++++++++++")
        try:
            # 调用1次登录方法，接收返回结果
            createdept_result=self.createdept.page_center_createdept()
            log.info(f"获取的文本内容为{createdept_result}")
            # 断言登录成功，失败则触发AssertionError
            assert '自动化测试部门' in  createdept_result,  "部门【自动化测试部门】创建失败！"
            # 部门新增的日志
            log.info("✅ 部门【自动化测试部门】创建成功 → ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except AssertionError as ae:
            # 单独捕获登录失败的断言异常，日志更精准
            log.info(f"❌ 部门【自动化测试部门】创建失败：{ae}")
            raise  # 抛出，让pytest标记用例失败

if __name__ == '__main__':
    Test_Center_Createdept()
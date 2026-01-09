#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:44
# @Author  : songyoukang
# @File    : Test_center_createuser.py
# @Software: PyCharm
from tool.get_log import GetLog
log=GetLog.get_logger()
import pytest
from page.page_in import Page_in
from base.getdriver import DriverUtil
class Test_Center_Updateuser():
    """业务层"""
    def setup(self):
        #获取driver
        self.driver=DriverUtil.get_driver()
        #获取统一入口类
        self.page_in=Page_in(self.driver)
        self.page_in.get_page_center_login().page_login_deleteuser()
        self.deleteuser=self.page_in.get_page_center_deleteuser()
    def teardown(self):
        DriverUtil.quit_driver()
    @pytest.mark.run(order=4)
    def test_center_deleteuser(self):
        log.info("++++++++++++++++开始执行删除用户操作+++++++++++++++++++++++")
        try:
            # 调用1次登录方法，接收返回结果
            deleteuser_result=self.deleteuser.page_center_deleteuser()
            log.info(f"获取的文本内容为{deleteuser_result}")
            # 断言登录成功，失败则触发AssertionError
            assert "智先生测试修改"  not in deleteuser_result, "【用户】删除失败！"
            # 登录成功的日志（格式更清晰）
            log.info(f"✅ 账号【智先生测试修改删除成功】 → ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except AssertionError as ae:
            # 单独捕获登录失败的断言异常，日志更精准
            log.info(f"❌ 账号【智先生测试修改删除成功】删除失败：{ae}")
            raise  # 抛出，让pytest标记用例失败

if __name__ == '__main__':
    Test_Center_Updateuser()
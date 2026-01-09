#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 16:40
# @Author  : songyoukang
# @File    : page_center_updateuser.py
# @Software: PyCharm
import time

from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Updateuser(Base):
    #点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    #点击编辑按钮
    def page_button_update(self):
        self.click_element(sysuser_update_button)
    #点击用户姓名修改
    def page_input_updatenickname(self,username):
        self.input_element(sysuser_update_username,username)
    #点击确定
    def page_button_updatetrue(self):
        self.click_element(sysuser_update_true)
    #修改成功文本
    def page_alert_text(self):
       return self.get_text_element(sysuser_update_ok)

    # ========== 业务组合测试 ==========
    def page_center_updateuser(self, username='智先生测试修改'):
        self.page_button_setting()
        self.page_button_update()
        self.page_input_updatenickname(username)
        time.sleep(3)
        self.page_button_updatetrue()
        return  self.page_alert_text()



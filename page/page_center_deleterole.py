#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 16:40
# @Author  : songyoukang
# @File    : page_center_updaterole.py
# @Software: PyCharm
import time

from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Deleterole(Base):
    #点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)

    # 点击角色管理
    def page_button_juese(self):
        self.click_element(sysrole_jueseguanli_delete)
    #点击删除按钮
    def page_button_delete(self):
        self.click_element(sysrole_delete_button)
    #点击确定删除
    def page_button_deletetrue(self):
        self.click_element(sysrole_delete_true)
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysrole_ok)

    # ========== 业务组合测试 ==========
    def page_center_deleterole(self):
        self.page_button_setting()
        self.page_button_juese()
        time.sleep(2)
        self.page_button_delete()
        time.sleep(2)
        self.page_button_deletetrue()
        return  self.page_alert_text()



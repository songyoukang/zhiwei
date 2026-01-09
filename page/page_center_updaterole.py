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
class Page_Center_Updaterole(Base):
    #点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    # 点击角色管理
    def page_button_juese(self):
        self.click_element(sysrole_jueseguanli_update)
    #点击编辑按钮
    def page_button_update(self):
        time.sleep(1)
        self.click_element(sysrole_update_button)
    #点击角色名称修改
    def page_input_updaterolekname(self,rolename):
        self.input_element(sysrole_update_rolename,rolename)
    #点击确定
    def page_button_updatetrue(self):
        self.click_element(sysrole_update_true)
        self.click_element(sysrole_update_res)
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysrole_update_ok)


    # ========== 业务组合测试 ==========
    def page_center_updaterole(self, rolename='自动化测试角色修改'):
        self.page_button_setting()
        self.page_button_juese()
        self.page_button_update()
        self.page_input_updaterolekname(rolename)
        time.sleep(3)
        self.page_button_updatetrue()
        return  self.page_alert_text()



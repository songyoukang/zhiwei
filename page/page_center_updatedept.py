#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 16:40
# @Author  : songyoukang
# @File    : page_center_updatedept.py
# @Software: PyCharm
import time
from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Updatedept(Base):
    #点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    # 点击部门管理
    def page_button_deptguanli(self):
        self.click_element(sysdept_update_deptguanli)
    #点击编辑按钮
    def page_button_update(self):
        time.sleep(1)
        self.click_element(sysdept_update_deptbutton)
    #点击部门名称修改
    def page_input_updatedeptkname(self,deptname):
        self.input_element(sysdept_update_deptname,deptname)
    #点击确定
    def page_button_updatetrue(self):
        self.click_element(sys_update_depttrue)
        self.click_element(sysdept_update_sreach)
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysdept_update_ok)

    # ========== 业务组合测试 ==========
    def page_center_updatedept(self, deptname='自动化测试部门修改'):
        self.page_button_setting()
        self.page_button_deptguanli()
        self.page_button_update()
        time.sleep(3)
        self.page_input_updatedeptkname(deptname)
        time.sleep(3)
        self.page_button_updatetrue()
        return  self.page_alert_text()



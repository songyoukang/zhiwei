#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:33
# @Author  : songyoukang
# @File    : page_center_createrole.py
# @Software: PyCharm
import time
from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Createrole(Base):
    """页面层"""
    # 点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    # 点击角色管理
    def page_button_role(self):
        self.click_element(sysrole_jueseguanli_button)
    # 点击新增角色按钮
    def page_button_create(self):
        self.click_element(sysrole_create_button)
    # 输入角色名
    def page_input_rolename(self,rolename):
        self.input_element(sysrole_create_rolename,rolename)
    #点击确定按钮
    def page_button_true(self):
        self.click_element(sysrole_create_true)
        self.click_element(sysrole_create_reatch)
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysrole_create_ok)

    # ========== 业务组合测试 ==========
    def page_center_createrole(self,createrolename='自动化测试角色'):
        log.info('正在创建角色，角色名：{}'.format(createrolename))
        self.page_button_setting()
        self.page_button_role()
        self.page_button_create()
        self.page_input_rolename(createrolename)
        self.page_button_true()
        return self.page_alert_text()



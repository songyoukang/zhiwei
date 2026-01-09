#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:33
# @Author  : songyoukang
# @File    : page_center_createdept.py
# @Software: PyCharm
import time
from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Createdept(Base):
    """页面层"""
    # 点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    # 点击部门管理
    def page_button_dept(self):
        self.click_element(sysdept_create_deptguanli)
    # 点击新增部门按钮
    def page_button_create(self):
        self.click_element(sysdept_create_button)
    # 输入部门名
    def page_input_deptname(self,deptname):
        self.input_element(sysdept_create_deptname,deptname)

    # 输入部门排序
    def page_input_deptdesc(self, deptdesc):
        self.input_element(sysdept_create_deptdesc, deptdesc)
    #点击确定按钮
    def page_button_true(self):
        self.click_element(sysdept_create_true)
        self.click_element(sysdept_create_sreach)
    #刷新页面
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysdept_create_ok)

    # ========== 业务组合测试 ==========
    def page_center_createdept(self,createdeptname='自动化测试部门',deptdesc=0):
        log.info('正在创建部门，部门名：{}'.format(createdeptname))
        self.page_button_setting()
        self.page_button_dept()
        self.page_button_create()
        self.page_input_deptname(createdeptname)
        self.page_input_deptdesc(deptdesc)
        time.sleep(1)
        self.page_button_true()
        return self.page_alert_text()



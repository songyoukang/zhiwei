#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2026/1/4 11:33
# @Author  : songyoukang
# @File    : page_center_createuser.py
# @Software: PyCharm
import time

from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
from page import *
class Page_Center_Createuser(Base):
    """页面层"""
    # 点击系统设置
    def page_button_setting(self):
        self.click_element(sys_setting)
    # 点击新增用户按钮
    def page_button_create(self):
        self.click_element(sysuser_create_button)
    # 输入用户名
    def page_input_nickname(self,nickname):
        self.input_element(sysuser_create_nickname,nickname)
    # 输入输户姓名
    def page_input_username(self,username):
        self.input_element(sysuser_create_username,username)
    # 选择角色
    def page_select_rolename(self):
        self.click_element(sysuser_create_rolename)
        self.click_element(sysuser_create_rolename1)
    # 输入联系电话
    def page_input_tellname(self,tellname):
        self.input_element(sysuser_create_tellname,tellname)
    # 输入密码
    def page_input_passwdname(self,passwdname):
        self.input_element(sysuser_create_passwdname,passwdname)
    # 输入确认密码
    def page_input_repasswdname(self,repasswdname):
        self.input_element(sysuser_create_repasswdname,repasswdname)
    #点击确定按钮
    def page_button_true(self):
        self.click_element(sysuser_create_true)
    #新增成功文本
    def page_alert_text(self):
       return self.get_text_element(sysuser_create_ok)

    # ========== 业务组合测试 ==========
    def page_center_createuser(self,createnickname='zxsautotest',createusername='智先生测试',tellname=1560629,createpasswd='qwer@1212',createrepasswdname='qwer@1212'):
        log.info('正在创建用户，用户名：{}，密码：{}'.format(createnickname,createpasswd))
        self.page_button_setting()
        self.page_button_create()
        self.page_input_nickname(createnickname)
        self.page_input_username(createusername)
        self.page_select_rolename()
        self.page_input_tellname(tellname)
        self.page_input_passwdname(createpasswd)
        self.page_input_repasswdname(createrepasswdname)
        self.page_button_true()
        time.sleep(3)
        return  self.page_alert_text()



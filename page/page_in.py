#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/8/28 10:07
# @Author  : songyoukang
# @File    : page_in.py
# @Software: PyCharm
from base.base import Base
from page.page_center_createdept import Page_Center_Createdept
from page.page_center_deletedept import Page_Center_Deletedept
from page.page_center_deleterole import Page_Center_Deleterole
from page.page_center_login import Page_Center_login
from page.page_center_createuser import Page_Center_Createuser
from page.page_center_updatedept import Page_Center_Updatedept
from page.page_center_updateuser import Page_Center_Updateuser
from page.page_center_deleteuser import Page_Center_Deleteuser
from page.page_center_createrole import Page_Center_Createrole
from page.page_center_updaterole import Page_Center_Updaterole
class Page_in(Base):
    def __init__(self, driver):
        self.driver = driver
    #登录测试业务组合
    def get_page_center_login(self):
        return Page_Center_login(self.driver)
    #新建系统用户业务组合
    def get_page_center_createuser(self):
        return Page_Center_Createuser(self.driver)
    # 系统修改用户业务组合
    def get_page_center_updateuser(self):
        return Page_Center_Updateuser(self.driver)
    #系统删除用户业务组合
    def get_page_center_deleteuser(self):
        return Page_Center_Deleteuser(self.driver)
    #新建系统角色业务组合
    def get_page_center_createrole(self):
        return Page_Center_Createrole(self.driver)
    # 系统修改角色业务组合
    def get_page_center_updaterole(self):
        return Page_Center_Updaterole(self.driver)
    # 系统删除角色业务组合
    def get_page_center_deleterole(self):
        return Page_Center_Deleterole(self.driver)
    # 新建系统部门业务组合
    def get_page_center_createdept(self):
        return Page_Center_Createdept(self.driver)
    # 系统修改部门业务组合
    def get_page_center_updatedept(self):
        return Page_Center_Updatedept(self.driver)
    # 系统删除部门业务组合
    def get_page_center_deletedept(self):
        return Page_Center_Deletedept(self.driver)
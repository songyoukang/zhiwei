#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 17:1011
# @Author  : songyoukang
# @File    : __init__.py.py
# @Software: PyCharm
"""自动化页面数据元素信息"""
#访问地址
from selenium.webdriver.common.by import By
"""登录元素信息"""
#PC端
web_url='http://10.10.200.180:28115/index'
#移动端
H5url='http://dev-demo.zxsit.com:35049/h5/pages/index/index'

#login登录页面元素
login_name=By.XPATH,"//*[@id='app']/div[1]/form/div[2]/div/div/input"
#登录用户
login_passwd=By.XPATH,"//*[@id='app']/div[1]/form/div[3]/div/div/input"
#登录密码
login_button= By.XPATH,'//*[@id="app"]/div[1]/form/div[4]'
#验证码
login_code=By.XPATH,'//*[@id="captcha"]/canvas[1]'
login_code1=By.XPATH,'//*[@id="captcha"]/canvas[2]'
# ===== 验证码刷新按钮=====
login_code_refresh = (By.XPATH, '//*[@id="captcha"]/div[2]')
"""中台页面元素"""
#点击系统设置
sys_setting=By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span"

"""中台新增用户信息"""
#全局获取用户list,断言统一业务是否存在
#sysuser_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[3]/table'

#点击新增用户按钮
sysuser_create_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[1]/div[2]/button[1]/span'
#输入用户名
sysuser_create_nickname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div/input'
#输入用户姓名
sysuser_create_username=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[2]/div/div/div[1]/input'
#选择用户角色
sysuser_create_rolename=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[3]/div/div/div/div/input'
sysuser_create_rolename1=By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[6]'
#输入用户电话
sysuser_create_tellname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[4]/div/div/div/input'
#输入用户密码
sysuser_create_passwdname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[6]/div/div/div/input'
#确认用户密码
sysuser_create_repasswdname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[7]/div/div/div/input'
#确定
sysuser_create_true=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/div/button[2]/span'
#断言统一业务是否存在
sysuser_create_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[3]'
"""中台修改用户信息"""
#编辑元素
sysuser_update_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[1]/span'
#修改用户姓名
sysuser_update_username=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[2]/div/div/div/input'
# #选择用户角色
# sys_update_rolename=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[3]/div/div/div/div/input'
# sys_update_rolename1=By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[9]/span'
# #输入用户电话
# sys_update_tellname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[4]/div/div/div/input'
# #输入用户密码
# sys_update_passwdname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[6]/div/div/div/input'
# #确认用户密码
# sys_update_repasswdname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[7]/div/div/div/input'
#确定
#确定按钮
sysuser_update_true=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/div/button[2]/span'
#断言统一业务是否存在
sysuser_update_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div'


"""删除用户元素信息"""
# 删除定位
sysuser_delete_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[2]/td[8]/div/button[3]/span')
# 删除确定文本
sysuser_delete_true = (By.XPATH, '/html/body/div[4]/div/div[3]/button[2]/span')
#断言统一业务是否存在
sysuser_delete_ok = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[3]')

"""新增角色信息"""
#全局获取角色list,断言是否存在
sysrole_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[3]/table/colgroup/col[2]'
#点击角色管理按钮元素
sysrole_jueseguanli_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[2]/a/li'
#新增按钮元素
sysrole_create_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/button[1]/span'
#角色名称输入框元素
sysrole_create_rolename=By.XPATH,'/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/input'
#排序输入框元素
sysrole_create_roledesc=By.XPATH,'/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/input'
#确定元素
sysrole_create_true=By.XPATH,'/html/body/div[4]/div/div[3]/div/button[2]/span'
#刷新页面
sysrole_create_reatch=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/button[1]/span'
#断言是否存在
sysrole_create_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div'
"""修改角色信息"""
#点击角色管理按钮元素
sysrole_jueseguanli_update=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[2]/a/li'
#点击角色编辑元素
sysrole_update_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/button[1]/span'
#角色名称输入框元素
sysrole_update_rolename=By.XPATH,'/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/input'
#确定元素
sysrole_update_true=By.XPATH,'/html/body/div[4]/div/div[3]/div/button[2]/span'
#刷新页面
sysrole_update_res=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/button[1]/span'
#断言是否存在
sysrole_update_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div'

"""删除角色元素信息"""
#点击角色管理按钮元素
sysrole_jueseguanli_delete=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[2]/a/li'
# 删除定位
sysrole_delete_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/button[2]/span')
# 确定文本
sysrole_delete_true = (By.XPATH, '/html/body/div[4]/div/div[3]/button[2]/span')


"""新增部门信息"""
#全局获取部门list,断言是否存在
sysdept_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]'

#点击部门管理按钮元素
sysdept_create_deptguanli=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[3]/a/li/span'
#新增按钮元素
sysdept_create_button=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[2]/button[1]/span'
#部门名称输入框元素
sysdept_create_deptname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/input'
#部门排序输入框元素
sysdept_create_deptdesc=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[3]/div/div[2]/form/div/div[3]/div/div/div/div/input'
#确定元素
sysdept_create_true=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span'
#点击搜索刷新页面
sysdept_create_sreach=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/button[1]/span'
#断言是否存在
sysdept_create_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]'

"""修改部门信息"""
#点击部门管理按钮元素
sysdept_update_deptguanli=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[3]/a/li/span'
#点击部门编辑元素
sysdept_update_deptbutton=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div/button[2]/span'
#输入部门名称
sysdept_update_deptname=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/input'
#确定元素
sys_update_depttrue=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[3]/div/div[3]/div/button[2]/span'
#点击搜索刷新页面
sysdept_update_sreach=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/button[1]/span'
#断言是否存在
sysdept_update_ok=By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]'
"""删除部门元素信息"""
#点击部门管理按钮元素
sysdept_delete_deptguanli=By.XPATH,'//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div/ul/div[1]/li/ul/div[3]/a/li/span'
# 删除定位
sysdept_delete_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[6]/div/button[4]/span')
# 确定文本
sysdept_delete_true = (By.XPATH, '/html/body/div[4]/div/div[3]/button[2]/span')

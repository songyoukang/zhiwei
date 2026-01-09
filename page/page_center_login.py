#!/usr/bin/env python1
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 17:11
# @Author  : songyoukang
# @File    : page_center_login.py
# @Software: PyCharm
import time
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLog
log=GetLog.get_logger()
from base.base import Base
import page
class Page_Center_login(Base):
    """页面层"""
    # 输入用户名
    def page_input_name(self, username):
        self.input_element(page.login_name, username)
    # 输入密码
    def page_input_password(self, passwd):
        self.input_element(page.login_passwd, passwd)
    #点击登录
    def page_click_button(self):
        self.click_element(page.login_button,)
    # 点击验证码刷新按钮
    def page_click_captcha_refresh(self):
        try:
            self.click_element(page.login_code_refresh)
            time.sleep(1)
            log.info("验证码已刷新")
        except Exception as e:
            log.info(f"刷新验证码失败：{e}")
    def _check_login_success(self):
        try:
            # 等待页面跳转（最多10秒）
            WebDriverWait(self.driver, 10).until(
                lambda x: "login" not in self.driver.current_url.lower()
            )
            current_url = self.driver.current_url
            log.info(f"✅ 登录成功：URL已跳转至 {current_url}")
            return True
        except Exception as e:
            log.info(f"❌ 登录失败：URL仍停留在登录页，{e}")
            return False
    def _retry_captcha_until_login_success(self, max_retry=100):
        """
        封装验证码重试逻辑：循环处理验证码，直到登录成功或达到最大重试次数
        :param max_retry: 最大重试次数，默认10次
        :return: 登录成功返回True，失败抛异常
        """
        retry_count = 0
        while retry_count < max_retry:
            retry_count += 1
            log.info(f"\n========== 验证码重试：第 {retry_count} 次 ==========")
            try:
                # 处理验证码（原有逻辑）
                self.handle_captcha()
            except Exception as e:
                log.info(f"第 {retry_count} 次验证码处理失败：{e}")
                self.page_click_captcha_refresh()
                time.sleep(1)
                continue  # 处理失败，刷新后重试
            # 验证码处理成功，检查是否登录成功
            if self._check_login_success():
                log.info(f" 第 {retry_count} 次验证码尝试：登录成功！")
                return True
            # 验证码拖动成功但登录失败，刷新重试
            log.info(f" 第 {retry_count} 次验证码拖动成功但登录失败，刷新重试...")
            self.page_click_captcha_refresh()
            time.sleep(1)
        # 超过最大重试次数，抛异常提示
        raise Exception(f"已重试{max_retry}次验证码，仍未登录成功！")
    # ========== 业务组合测试 ==========
    #登录业务组合
    def page_center_login(self, username, passwd):
        log.info('正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        # 1. 首次输入账号密码（仅执行1次）
        log.info("========== 首次登录：输入账号密码 ==========")
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()
    # 新增用户业务组合
    def page_login_createuser(self, username='songyoukang', passwd='qwer@1212'):
        log.info('新增用户测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()
    # 修改用户业务组合
    def page_login_updateuser(self, username='zxsautotest', passwd='qwer@1212'):
        log.info('修改用户测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()
    #删除用户业务组合
    def page_login_deleteuser(self, username='songyoukang', passwd='qwer@1212'):
        log.info('删除用户测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    # 新增角色业务组合
    def page_login_createrole(self, username='songyoukang', passwd='qwer@1212'):
        log.info('新增角色测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    # 修改角色业务组合
    def page_login_updaterole(self, username='songyoukang', passwd='qwer@1212'):
        log.info('修改角色测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    #删除角色业务组合
    def page_login_deleterole(self, username='songyoukang', passwd='qwer@1212'):
        log.info('删除角色测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    # 新增部门业务组合
    def page_login_createdept(self, username='songyoukang', passwd='qwer@1212'):
        log.info('新增部门测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    # 修改部门业务组合
    def page_login_updatedept(self, username='songyoukang', passwd='qwer@1212'):
        log.info('修改部门测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()

    # 删除部门业务组合
    def page_login_deletedept(self, username='songyoukang', passwd='qwer@1212'):
        log.info('删除部门测试用例开始：\n正在调用智维中台的登录业务，用户名：{}，密码：{}'.format(username, passwd))
        self.page_input_name(username)
        self.page_input_password(passwd)
        self.page_click_button()
        # 2. 调用封装的验证码重试方法
        return self._retry_captcha_until_login_success()
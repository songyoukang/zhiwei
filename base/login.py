#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 17:50
# @Author  : songyoukang
# @File    : login.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class CaptchaLogin():
    def perform_login(self):
        driver=webdriver.Chrome()
        driver.get('http://10.10.200.180:28115/login')
        driver.refresh()
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').send_keys('songyoukang')
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[3]/div/div/input').send_keys('qwer@1212')
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[4]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="captcha"]/canvas[2]')
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[3]/div/div/div/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text()='第三方工程师']").click()
        time.sleep(10)
        # lists=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]').text
        # print(lists)
        # assert "自动化测试部门修改" in lists, "目标文本未找到，断言失败"
        # print("获取成功")
        # driver.quit()


CaptchaLogin().perform_login()

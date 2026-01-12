#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 17:50
# @Author  : songyoukang
# @File    : login.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# class CaptchaLogin():
#     def perform_login(self):
#         driver=webdriver.Chrome()
#         driver.get('http://10.10.200.180:28115/login')
#         driver.refresh()
#         driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[2]/div/div/input').send_keys('songyoukang')
#         driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[3]/div/div/input').send_keys('qwer@1212')
#         driver.find_element_by_xpath('//*[@id="app"]/div[1]/form/div[4]').click()
#         time.sleep(1)
#         driver.find_element_by_xpath('//*[@id="captcha"]/canvas[2]')
#         time.sleep(4)
#         driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span').click()
#         time.sleep(5)
#         driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[2]/form/div[1]/div[3]/div/div/div/div/input').click()
#         time.sleep(1)
#         driver.find_element_by_xpath("//*[text()='第三方工程师']").click()
#         time.sleep(10)
#         # lists=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]').text
#         # print(lists)
#         # assert "自动化测试部门修改" in lists, "目标文本未找到，断言失败"
#         # print("获取成功")
#         # driver.quit()
# CaptchaLogin().perform_login()

# 在testgettask.py中添加
import os
import sys
import socket
import logging
import requests
from requests.exceptions import RequestException

# 配置日志，打印详细调试信息
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------- 配置项（请修改这里）--------------------------
TARGET_URL = "http://127.0.0.1:8080/api"  # 替换为你的目标服务地址
TARGET_HOST = "127.0.0.1"                  # 目标IP/主机名
TARGET_PORT = 8000                         # 目标端口
# ------------------------------------------------------------------------

def print_system_info():
    """打印系统和网络基础信息"""
    logging.info("===== 系统基础信息 =====")
    logging.info(f"Python版本: {sys.version}")
    logging.info(f"当前工作目录: {os.getcwd()}")
    logging.info(f"请求库requests版本: {requests.__version__}")

def test_tcp_connect():
    """测试TCP端口连通性（最底层网络验证）"""
    logging.info("\n===== TCP端口连通性测试 =====")
    try:
        # 创建TCP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # 10秒超时
        result = sock.connect_ex((TARGET_HOST, TARGET_PORT))
        if result == 0:
            logging.info(f"✅ 成功连接到 {TARGET_HOST}:{TARGET_PORT}")
        else:
            logging.error(f"❌ 无法连接到 {TARGET_HOST}:{TARGET_PORT}，错误码: {result}")
            logging.error("错误码说明：10061=目标服务拒绝连接，10060=连接超时，0=成功")
        sock.close()
    except Exception as e:
        logging.error(f"TCP连接测试异常: {type(e).__name__} - {str(e)}")

def test_http_request():
    """测试HTTP/HTTPS请求（模拟你的业务请求）"""
    logging.info("\n===== HTTP请求测试 =====")
    try:
        # 关闭代理，避免代理干扰
        proxies = {"http": None, "https": None}
        # 发送请求，关闭重定向，设置超时
        response = requests.get(
            TARGET_URL,
            proxies=proxies,
            timeout=10,
            allow_redirects=False
        )
        logging.info(f"✅ 请求成功，状态码: {response.status_code}")
        logging.info(f"响应头: {dict(response.headers)}")
        logging.info(f"响应内容（前200字符）: {response.text[:200]}")
    except RequestException as e:
        logging.error(f"❌ HTTP请求失败: {type(e).__name__} - {str(e)}")
        # 打印更详细的错误信息
        if hasattr(e, 'response') and e.response is not None:
            logging.error(f"响应状态码: {e.response.status_code}")

if __name__ == "__main__":
    # 执行所有测试
    print_system_info()
    test_tcp_connect()
    test_http_request()
    logging.info("\n===== 测试结束 =====")
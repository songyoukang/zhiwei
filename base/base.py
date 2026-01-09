#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/27 15:09
# @Author  : songyoukang
# @File    : base.py
# @Software: PyCharm
import time
from config import BASE_PATH
import os
import allure
import cv2
import numpy as np  # 新增：验证码图片处理依赖
import base64
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # 新增：滑块拖动依赖
from selenium.webdriver.support import expected_conditions as EC

from tool.get_log import GetLog

log=GetLog.get_logger()

from page.__init__ import login_code, login_code1
class Base():
    """基类"""
    def __init__(self,driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver=driver
    #查找元素方法
    def find_element(self,loc):
        log.info('正在查找元素：{}'.format(loc))
        return WebDriverWait(self.driver,timeout=10,poll_frequency=0.5).until((lambda x:x.find_element(*loc)))
    #点击方法
    def click_element(self,loc):
        log.info('正在对元素：{}执行点击操作'.format(loc))
        self.find_element(loc).click()
    #输入方法
    def input_element(self,loc,value):
        log.info('正在对:{}元素输入框执行清空操作'.format(loc))
        el=self.find_element(loc)
        el.clear()
        log.info('正在对：{}元素执行输入：{}操作'.format(loc,value))
        el.send_keys(value)
    #下拉框处理
    def select_element(self,loc,value):
        element=self.find_element(loc)
        select = Select(element)
        select.select_by_value(value)

    #获取元素文本
    def get_text_element(self,loc):
        log.info('正在获取元素：{}的文本，内容为：{}'.format(loc,self.find_element(loc).text))
        return self.find_element(loc).text
    #元素页面截图
    def base_get_img(self):
        log.error('断言出错，正在执行截图操作')
        self.driver.get_screenshot_as_file("../zhiwei_img/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        #调用图片写入到报告方法
        log.error('断言出错，正在将图片写入allure报告操作：')
        self.__base_write_img()
    #将图片写入到报告方法中(私有)
    def __base_write_img(self):
        with open("../zhiwei_img/error.png",'rb') as f:
            #调用allure报告方法附件描述方法
            allure.attach("错误原因",f.read(),allure.attach.type.PNG)
    # ========== 新增：验证码处理逻辑（整合到Base类中） ==========
    @staticmethod
    def calculate_slider_position(image_path,threshold_area = 1300,threshold_perimeter = 130):
        log.info('正在获取计算验证码滑块位置')
        """计算滑块位置"""
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        if image is None:
            raise Exception(f"验证码图片读取失败：{image_path}")
        blurred = cv2.GaussianBlur(image, (5, 5), 0, 0)
        canny = cv2.Canny(blurred, 50, 100)
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            length = cv2.arcLength(contour, True)
            if area > threshold_area and length > threshold_perimeter:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #save_path = r"C:\Users\syk19\Desktop\ZXS_UI\zhiwei_img\captcha_processed.jpg"
                save_path = os.path.join(BASE_PATH, "zhiwei_img", "captcha_processed.jpg")
                cv2.imwrite(save_path, image)
                return x
        return 0

    def handle_captcha(self):
        log.info('正在处理验证码,获取到验证码画布数据')
        """
        处理验证码（实例方法，直接复用self.driver，无需传参）
        替代原perform_login方法，更贴合Base层语义
        """
        # if not self.driver:
        #     raise ValueError("driver对象无效！")
        # time.sleep(1)
        # 定位验证码画布（使用统一元素login_code）
        try:
            canvas_ele = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(login_code)
            )
        except Exception as e:
            raise Exception(f"验证码画布定位失败：{e}")
        # 执行JS获取画布Base64数据
        script = """
        var canvas = arguments[0];
        return canvas.toDataURL('image/png');
        """
        image_data_url = self.driver.execute_script(script, canvas_ele)
        if not image_data_url:
            raise Exception("未获取到验证码画布数据")

        # 保存验证码图片1
        image_base64 = image_data_url.split(',')[1]
        image_binary = base64.b64decode(image_base64)
        #save_path = r"C:\Users\syk19\Desktop\ZXS_UI\zhiwei_img\captcha_image.png"
        save_path = os.path.join(BASE_PATH, "zhiwei_img", "captcha_image.jpg")
        with open(save_path, 'wb') as f:
            f.write(image_binary)
        log.info('正在计算滑块位置数据')

        # 计算滑块位置
        slider_position = self.calculate_slider_position(save_path)
        if slider_position == 0:
            raise Exception("未识别到滑块位置")
        # 拖动滑块（使用统一元素login_code1）
        small_image = self.driver.find_element(*login_code1)
        log.info('正在获取滑块拖动位置：{}'.format(small_image))
        new_position = int(slider_position * 340 / 672 - small_image.location['x'])
        # 模拟滑块拖动
        log.info('正在模拟鼠标推动滑块位置')
        action = ActionChains(self.driver)
        action.click_and_hold(small_image).perform()
        action.move_by_offset(xoffset=slider_position + 7, yoffset=-1).perform()
        action.move_by_offset(xoffset=0.1, yoffset=2).perform()
        action.release().perform()
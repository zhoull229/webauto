"""
author：lulu
time:2021/3/22  19:22

"""
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.set_log import log
from common.set_path import error_pic_path


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, loc, desc=None):
        '''
        查找元素
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        '''
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            log.error(f"查找元素：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"查找元素：----{desc}----成功")
        return ele

    def click_element(self, loc, desc):
        '''
        点击元素
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        '''
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            log.error(f"点击元素：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"点击元素：----{desc}----成功")

    def input_send_keys(self, loc, value, desc):
        '''
        输入框输入元素
        :param loc: 元素定位器
        :param value: 要输入的值
        :param desc: 元素的描述
        :return:
        '''
        try:
            self.driver.find_element(*loc).send_keys(value)
        except Exception as e:
            log.error(f"往输入框输入：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"往输入框输入：----{desc}----成功")

    def get_element_text(self, loc, desc):
        '''
        获取元素的text值
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        '''
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            log.error(f"获取元素的值：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"获取元素的值：----{desc}----成功")
        return text

    def wait_element_visibility(self, loc, desc):
        '''
        等待元素可见
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, 15, 0.5).until(
                EC.visibility_of_element_located(loc)
            )
        except Exception as e:
            log.error(f"等待元素可见：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"等待元素可见：----{desc}----成功")
        return ele

    def wait_element_clickable(self, loc, desc):
        '''
        等待元素可点击
        :param loc: 元素定位器
        :param desc: 元素的描述
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, 15, 0.5).until(
                EC.element_to_be_clickable(loc)
            )
        except Exception as e:
            log.error(f"等待元素可点击：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"等待元素可点击：----{desc}----成功")
        return ele

    def execute_scriptcode(self, js_code, desc,*arguments):
        '''
        通过js代码操作元素
        :param js_code: js代码
        :param desc: 元素的描述
        :param *arguments: arguments值
        :return:
        '''
        try:
            self.driver.execute_script(js_code, *arguments)
        except Exception as e:
            log.error(f"执行js代码：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"执行js代码：----{desc}----成功")
    def move_element_by_offset(self, ele,xoffset=0,yoffset=0,desc=None):
        '''
        移动鼠标到相对位置
        :param ele: 要移动的元素
        :param xoffset: 相对x坐标的值
        :param yoffset: 相对y坐标的值
        :param desc: 元素的描述
        :return:
        '''
        try:
            action = ActionChains(self.driver)
            action.click_and_hold(ele)
            action.move_by_offset(xoffset=xoffset, yoffset=yoffset)
            action.release()
            action.perform()
        except Exception as e:
            log.error(f"移动元素到相对位置：----{desc}----失败")
            log.exception(e)
            self.error_screenshot(desc)
            raise e
        else:
            log.info(f"移动元素到相对位置：----{desc}----成功")

    def error_screenshot(self, desc):
        '''
        截图
        :param desc: 元素的描述
        :return:
        '''
        data = time.strftime("%Y-%m-%d_%H.%M.%S_")
        filename = data + desc + ".png"
        filepath = os.path.join(error_pic_path, filename)
        try:
            self.driver.save_screenshot(filepath)
        except Exception as e:
            log.error(f"对{desc}操作截图----截图失败")
            log.exception(e)
            raise e
        else:
            log.info(f"对{desc}操作截图----截图成功，图片名为{filename}")

    def select_data_by_text(self, loc, text, desc):
        '''
        select选择框根据选项的text值选择元素:只支持select标签
        :param loc: 元素定位器
        :param text: 选项的text值
        :param desc: 元素的描述
        :return:
        '''
        try:
            ele = self.get_element(loc, desc)
            select = Select(ele)
            select.select_by_visible_text(text)
        except Exception as e:
            log.error(f"select选择框根据text选择元素：----{desc}----失败")
            log.exception(e)
            raise e
        else:
            log.info(f"select选择框根据text选择元素：----{desc}----成功")

    def select_data_by_value(self, loc, value, desc):
        '''
        select选择框根据选项的value值选择元素：只支持select标签
        :param loc: 元素定位器
        :param text: 选项的value值
        :param desc: 元素的描述
        :return:
        '''
        try:
            ele = self.get_element(loc, desc)
            select = Select(ele)
            select.select_by_value(value)
        except Exception as e:
            log.error(f"select选择框根据value选择元素：----{desc}----失败")
            log.exception(e)
            raise e
        else:
            log.info(f"select选择框根据value选择元素：----{desc}----成功")

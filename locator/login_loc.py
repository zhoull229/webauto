"""
author：lulu
time:2021/3/22  19:52

"""
from selenium.webdriver.common.by import By


class LoginLoc():
    # 账号输入框
    user_input_loc = (By.XPATH, "//input[@placeholder='账号']")
    # 密码输入框
    pwd_input_loc = (By.XPATH, "//input[@placeholder='密码']")
    # 验证码输入框
    valid_input_loc = (By.XPATH, "//input[@placeholder='验证码']")
    # 验证码图片
    valid_pic_loc = (By.XPATH, "//img[@class='security_img']")
    # 点击登录
    login_loc = (By.XPATH, "//button[@class='el-button login_btn el-button--primary']")
    # 账号为空文案提示
    user_error_info = (By.XPATH, "//input[@placeholder='账号']/../../div[@class='el-form-item__error']")
    # 密码为空文案提示
    pwd_error_info = (By.XPATH, "//input[@placeholder='密码']/../../div[@class='el-form-item__error']")
    # 验证码为空文案提示
    valid_error_info = (By.XPATH, "//input[@placeholder='验证码']/../../div[@class='el-form-item__error']")
    # 悬浮窗错误提示元素
    popup_error_info = (By.XPATH, "//p[@class='el-message__content']")
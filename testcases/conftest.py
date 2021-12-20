"""
author：lulu
time:2021/3/20  11:02

"""
from selenium import webdriver
import pytest
from selenium.webdriver import ChromeOptions
from datas.global_data import driver_login_url, driver_index_url
from page.loginPage import LoginPage


def create_driver(is_headers=True):
    """
    启动driver:默认启动浏览器窗口，is_headers设为False则已无头模式运行
    :param is_headers:  True  or  False
    :return:
    """
    if is_headers:
        driver = webdriver.Chrome()
    else:
        # 设置无头哦浏览器模式
        options = ChromeOptions()
        # 无头模式
        options.add_argument('--headless')
        # 设置窗口大小（无头模式下maximize_window()无法将窗口最大化，需要通过下面的启动参数去设置窗口大小）
        options.add_argument("--window-size=1920,1050")
        # 禁用GPU（可选）
        options.add_argument('--disable-gpu')
        # 非沙箱环境（可选）
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope="function")
def open_browser():
    """打开浏览器"""
    driver = create_driver(is_headers=False)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def skipvalid_login_success():
    """跳过验证码登录成功"""
    driver = create_driver(is_headers=False)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(driver_login_url)
    LoginPage(driver).writeto_sessionStorage()
    driver.get(driver_index_url)
    yield driver
    driver.quit()

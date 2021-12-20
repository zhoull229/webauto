"""
author：lulu
time:2021/3/19  16:04

"""
import allure
import pytest
from page.loginPage import LoginPage
from page.driver_infoPage import Driver_InfoPage
from datas.login_data import LoginData
from datas.global_data import driver_login_url, driver_index_url

@allure.story("登录页面")
class TestLogin():
    @allure.title("登录页--输入账号为空")
    @pytest.mark.parametrize("case", LoginData.login_tip_usererror_data)
    def test_login_pop_usererror(self, case, open_browser):
        """输入账号为空"""
        driver = open_browser
        driver.get(driver_login_url)
        login_page = LoginPage(driver)
        login_page.login(case["user"], case["pwd"], case["valid"])
        res = login_page.get_tip_usererror_info()
        assert res == case["expected"]

    @allure.title("登录页--输入密码为空")
    @pytest.mark.parametrize("case", LoginData.login_tip_pwderror_data)
    def test_login_pop_pwderror(self, case, open_browser):
        """输入密码为空"""
        driver = open_browser
        driver.get(driver_login_url)
        login_page = LoginPage(driver)
        login_page.login(case["user"], case["pwd"], case["valid"])
        res = login_page.get_tip_pwderror_info()
        assert res == case["expected"]

    @allure.title("登录页--输入验证码为空")
    @pytest.mark.parametrize("case", LoginData.login_tip_validerror_data)
    def test_login_pop_validerror(self, case, open_browser):
        """输入验证码为空"""
        driver = open_browser
        driver.get(driver_login_url)
        login_page = LoginPage(driver)
        login_page.login(case["user"], case["pwd"], case["valid"])
        res = login_page.get_tip_validerror_info()
        assert res == case["expected"]

    @allure.title("登录页--输入验证码错误")
    @pytest.mark.parametrize("case", LoginData.login_popup_error_data)
    def test_login_validpoperror(self, case, open_browser):
        """输入验证码错误"""
        driver = open_browser
        driver.get(driver_login_url)
        login_page = LoginPage(driver)
        login_page.login(case["user"], case["pwd"], case["valid"])
        res = login_page.get_loginpopup_error_info()
        assert res == case["expected"]

    @allure.title("登录页--通过跳过验证码这一步，直接登录成功")
    def test_login_success(self, open_browser):
        """通过跳过验证码这一步，直接登录成功"""
        driver = open_browser
        driver.get(driver_login_url)
        LoginPage(driver).writeto_sessionStorage()
        driver.get(driver_index_url)
        driver_info_page = Driver_InfoPage(driver)
        assert driver_info_page.is_login_success() == True

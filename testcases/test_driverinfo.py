"""
author：lulu
time:2021/3/23  14:40

"""
import time

import allure
import pytest
from datas.query_driver_data import QueryDriverDate
from page.driver_infoPage import Driver_InfoPage
@allure.story("司机基础信息页面")
class TestDriverInfo():
    # @allure.title("司机基础信息页面--根据司机id查询司机信息")
    # @pytest.mark.parametrize("case",QueryDriverDate.driver_data)
    # def test_driverinfo_by_id(self,case,skipvalid_login_success):
    #     '''根据司机id查询司机信息'''
    #     driver=skipvalid_login_success
    #     Driver_InfoPage(driver).query_by_driverid(case["driverID"])
    #     text=Driver_InfoPage(driver).query_by_driverid_success()
    #     assert text==case["driverID"]
    #
    # @allure.title("司机基础信息页面--根据司机出车状态"出车(离线)"查询司机信息")
    # def test_driverinfo_by_carstate(self,skipvalid_login_success):
    #     '''根据司机出车状态"出车(离线)"查询司机信息'''
    #     driver=skipvalid_login_success
    #     Driver_InfoPage(driver).query_by_car_state()
    #     time.sleep(3)
    #     result=Driver_InfoPage(driver).query_by_car_state_success()
    #     assert result==True
    @allure.title("司机基础信息页面--根据所属机构查询司机信息")
    def test_driverinfo_by_org(self,skipvalid_login_success):
        '''根据所属机构查询司机信息'''
        driver=skipvalid_login_success
        Driver_InfoPage(driver).query_by_org()
        time.sleep(10)





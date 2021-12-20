"""
author：lulu
time:2021/3/22  17:26

"""
import time

from selenium.webdriver.common.keys import Keys

from locator.driver_list_loc import DriverListLoc
from common.base_page import BasePage


class Driver_InfoPage(BasePage):
    '''司机基础信息列表页面'''

    def is_login_success(self):
        '''判断是否登录成功'''
        try:
            self.get_element(DriverListLoc.menu_driverinfo_loc, "司机基础信息页_导航栏")
        except:
            return False
        else:
            return True

    def query_by_driverid(self, driverid):
        '''根据司机id查询信息'''
        self.input_send_keys(DriverListLoc.driverid_loc, f'{driverid}', "司机基础信息页_输入司机id")
        self.click_element(DriverListLoc.driver_query_loc, "司机基础信息页_点击查询按钮")

    def query_by_driverid_success(self):
        '''判断根据司机id查询信息是否成功'''
        try:
            text = self.get_element_text(DriverListLoc.list_driverid_loc, "司机基础信息页_列表司机id的值")
        except:
            return False
        else:
            return text

    def query_by_car_state(self):
        '''根据司机出车状态查询信息'''
        self.click_element(DriverListLoc.car_state_loc, "司机基础信息页_点击出车状态按钮")
        self.click_element(DriverListLoc.car_offline_loc, "司机基础信息页_点击出车(离线)选项")
        ele = self.get_element(DriverListLoc.driver_query_loc, "司机基础信息页_获取查询按钮")
        # 因为查询按钮被覆盖，无法点击到，所以使用js代码进行点击
        # self.driver.execute_script("arguments[0].click();", ele)
        self.execute_scriptcode("arguments[0].click();", "司机基础信息页_点击查询按钮", ele)

    def query_by_car_state_success(self):
        '''判断根据司机出车状态"出车(离线)"查询信息是否成功'''
        try:
            # 获取列表所有数据的出车状态
            eles = self.driver.find_elements(*DriverListLoc.list_carstate_loc)
            eles_text = [i.text for i in eles]
            # 所有出车状态都为出车(离线)时，断定为成功
            for i in eles_text:
                assert i == "出车(离线)"
        except:
            return False
        else:
            return True

    def query_by_org(self):
        '''根据所属机构查询司机信息'''
        self.click_element(DriverListLoc.org_loc,"司机基础信息页_下拉框：所属机构按钮")
        ele=self.get_element(DriverListLoc.down_loc,"司机基础信息页_滑动省市的下拉框")
        a=ele.location
        print(a)
        self.move_element_by_offset(ele,0,100,"司机基础信息页_滑动省市的下拉框")

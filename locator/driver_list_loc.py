"""
author：lulu
time:2021/3/23  10:22

"""
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class DriverListLoc(BasePage):
    # 导航栏---司机基础信息
    menu_driverinfo_loc = (By.XPATH, "//span[text()='司机基础信息']")
    # 查询框--司机id
    driverid_loc = (By.XPATH, "//input[@placeholder='司机ID']")
    # 查询按钮
    driver_query_loc = (By.XPATH, "//span[text()='查询']")
    # 下拉框--出车状态按钮
    car_state_loc = (By.XPATH, "//input[@placeholder='出车状态']")
    # 下拉框--出车状态按钮--上一级
    car_state_above_loc = (By.XPATH, "//input[@placeholder='出车状态']/..")
    # 下拉框--出车(离线)选项
    car_offline_loc = (By.XPATH, "//div[@class='el-select-dropdown el-popper']//span[text()='出车(离线)']")
    # 下拉框--所属机构按钮
    org_loc=(By.XPATH,"//div[@class='el-cascader']//input[@type='text' ]")
    # 下拉框--所属机构第一列选项的下滑按钮
    down_loc=(By.XPATH,"//div[@class='el-scrollbar el-cascader-menu']/div[@class='el-scrollbar__bar is-vertical']/div[@class='el-scrollbar__thumb']")
    # 列表只有一条数据时：表单属性--司机id
    list_driverid_loc = (By.XPATH, "//td[@class='el-table_1_column_2 is-center  id-column']/div[@class='cell']")
    # 列表多条数据：表单属性--出车状态
    list_carstate_loc = (
    By.XPATH, "//td[@class='el-table_1_column_6 is-center  dispatchStatus-column']/div[@class='cell']")

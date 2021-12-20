"""
author：lulu
time:2021/3/20  11:10

"""
from common import get_token
from common.base_page import BasePage
from locator.login_loc import LoginLoc
from PIL import Image
import pytesseract


class LoginPage(BasePage):
    '''登录页面'''

    def login(self, user, pwd, valid):
        '''登录操作'''
        # 输入账号
        self.input_send_keys(LoginLoc.user_input_loc, user, "登录页_输入账号")
        # 输入密码
        self.input_send_keys(LoginLoc.pwd_input_loc, pwd, "登录页_输入账号")
        # 输入验证码
        self.input_send_keys(LoginLoc.valid_input_loc, valid, "登录页_输入账号")
        # 点击登录
        self.click_element(LoginLoc.login_loc, "登录页_点击登录按钮")

    def writeto_sessionStorage(self):
        '''向sessionstorage写入登录后的数据用来跳过登录'''
        # 获取调用接口得到的token值
        token = get_token.token
        # 向sessionstorage内写入一个数据
        obj = f'{{"id":643,"loginName":"15817266021","userName":"周露露","token":"{token}","loginTime":"2021-03-22 14:45:28","needUpdatePassword":false}}'
        js = f"sessionStorage.setItem('_ccmUser',JSON.stringify({obj}));"
        self.execute_scriptcode(js, "登录页_向sessionstorage内写入数据")

    def get_tip_usererror_info(self):
        """获取账号为空文案错误提示"""
        return self.wait_element_visibility(LoginLoc.user_error_info, "登录页_账号为空").text

    def get_tip_pwderror_info(self):
        """获取密码为空文案错误提示"""
        return self.wait_element_visibility(LoginLoc.pwd_error_info, "登录页_密码为空").text

    def get_tip_validerror_info(self):
        """获取验证码为空文案错误提示"""
        return self.wait_element_visibility(LoginLoc.valid_error_info, "登录页_验证码为空").text

    def get_loginpopup_error_info(self):
        """获取登录页_验证码不正确或已失效提示"""
        return self.wait_element_visibility(LoginLoc.popup_error_info, "登录页_验证码不正确或已失效提示").text

    # # 识别成功率低，暂不可用
    # def get_valid_pic(self):
    #     """截取图片验证码保存到本地，通过ocr识别获取验证码上的数字"""
    #     self.driver.save_screenshot(r"D:\PycharmProject\web_auto\datas\valid.png")
    #     #获取验证码图片
    #     valid_pic=self.driver.find_element(*self.valid_pic_loc)
    #     #验证码的坐标
    #     loc=valid_pic.location
    #     #验证码的大小
    #     size=valid_pic.size
    #     #图片4个点的位置
    #     lefttop_x=loc["x"]
    #     lefttop_y=loc["y"]
    #     rigthdown_x=lefttop_x+size["width"]
    #     rigthdown_y=lefttop_y+size["height"]
    #     #截取验证码图片保存
    #     image=Image.open(r"D:\PycharmProject\web_auto\datas\valid.png")
    #     new_image=image.crop((lefttop_x,lefttop_y,rigthdown_x,rigthdown_y))
    #     new_image.save(r"D:\PycharmProject\web_auto\datas\new_valid.png")
    #     open_new_image = Image.open(r"D:\PycharmProject\web_auto\datas\new_valid.png")
    #     valid = pytesseract.image_to_string(open_new_image, lang='eng',
    #                 config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    #     print(valid)
    #     return valid

"""
author：lulu
time:2021/3/20  14:11

"""


class LoginData:
    # 账号为空数据
    login_tip_usererror_data = [
        {"user": "", "pwd": "123456", "valid": "1111", "expected": "账号不能为空"}
    ]
    # 密码为空数据
    login_tip_pwderror_data = [
        {"user": "xxxxxxxxxxx", "pwd": "", "valid": "1111", "expected": "密码不能为空"}
    ]
    # 验证码为空数据
    login_tip_validerror_data = [
        {"user": "xxxxxxxxxxx", "pwd": "123456", "valid": "", "expected": "验证码不能为空"}
    ]
    # 弹窗报错提示数据
    login_popup_error_data = [
        {"user": "xxxxxxxxxxx", "pwd": "123456", "valid": "0000", "expected": "验证码不正确或已失效"},
    ]

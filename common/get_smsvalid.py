"""
author：lulu
time:2021/3/20  17:55

"""
import requests
from conf import conf
from jsonpath import jsonpath
class GetValid():
    #获取后台短信验证码
    def getbackground_valid(self,env="get_code?index=1"):
        url=conf.sms_url+env
        print(url)
        respon=requests.get(url=url)
        # print(respon.json())
        background= jsonpath(respon.json(),"$.data.background")[0]#返回一个列表
        for i in background:
           if i["phone"]=="xxxxxxxxxxx":#手机号
               return i["verifyCode"]

valid=GetValid().getbackground_valid()




"""
author：lulu
time:2020/12/17  10:57

"""
import requests
import json
from rediscluster import RedisCluster
from conf import conf

class Login():

    def get_keyCode(self):
        # 调用获取验证码接口获得keyCode
        datavalid = {"op": "select", "token": ""}
        valid_url = conf.imp_manager_url + "/system/getValidateCode"
        resvalid = requests.post(url=valid_url, json=datavalid)
        res_content = resvalid.json()
        keycode = res_content["data"]
        keycode1 = json.loads(keycode)["keyCode"]
        return keycode1

    def get_redis_valid(self):
        # 连接redis集群,获取验证码
        st = [{"host": conf.imp_redies_url, "port": conf.imp_redies_port}]
        conn = RedisCluster(startup_nodes=st, password=conf.imp_redies_pwd)
        keycode = self.get_keyCode()
        key1 = "xxx_xxx_" + keycode#文件存储格式+keycode
        key = conn.get(key1)
        authcode = eval(str(key)[2:-1])["authCode"]
        return authcode, keycode

    def get_token(self):
        # 调用登录接口获取token
        login_url = conf.imp_manager_url + "/system/login"
        user = conf.user
        password = conf.pwd
        authCode_keyCode = self.get_redis_valid()
        data1 = f"{{'loginName':{user},'password':{password},'keyCode':{authCode_keyCode[1]},'authCode':{authCode_keyCode[0]}}}"
        data = {"data": data1,
                "op": "select",
                "token": ""}
        response = requests.request(method="post", url=login_url, json=data)
        res = response.json()
        token = json.loads(res["data"])["token"]
        return token

token=Login().get_token()
"""
author：lulu
time:2021/2/25  9:34

"""
import pytest
from common.set_path import report_path

pytest.main(['-s','-v',f'--alluredir={report_path}',
             '--reruns','3',
             '--reruns-delay','5'])
#查看报告：命令行输入allure serve ./reports
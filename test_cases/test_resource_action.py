# coding:utf-8
# 2021/2/19 18:31
# Author:dsw

import time
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.my_resource_add_page import AddPage
from PageObjects.resource_action_page import ResourceActionPage
from selenium import webdriver
from PageObjects.operation_depart_page import OperationPage
from test_data import Global_Datas as GD
from test_data import login_datas as lds
import ddt


@ddt.ddt
class test_add_resource(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*lds.success)

    def tearDown(self):
        self.driver.quit()



    # 添加预约访
    def test_add_appointment(self):

        OperationPage(self.driver).enter_operation_page()

        for i in range(1, 10):
            resource_data = AddPage(self.driver).add_resource_data()
            OperationPage(self.driver).add_resource()
            AddPage(self.driver).add_resource(*resource_data)
            ResourceActionPage(self.driver).appointment(resource_data[0])
            time.sleep(2)
            print(i)








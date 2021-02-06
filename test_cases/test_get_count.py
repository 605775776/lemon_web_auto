# coding:utf-8
# 2021/2/5 10:50
# Author:dsw

# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import time
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.operation_depart_page import OperationPage
from PageObjects.my_resource_add_page import AddPage
from PageObjects.resource_action_page import ResourceActionPage
from PageObjects.index_page import IndexPage
from selenium import webdriver
from test_data import Global_Datas as GD
from test_data import login_datas as lds
from test_data import resource_data as rd
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

    def test_add_1resource(self):
        OperationPage(self.driver).enter_operation_page()
        time.sleep(2)
        (a, b, c, d) = OperationPage(self.driver).get_resource_count()

        OperationPage(self.driver).add_resource()
        resource_data = AddPage(self.driver).add_resource_data()
        print(resource_data)
        AddPage(self.driver).add_resource(*resource_data)
        time.sleep(2)
        (e, f, g, h) = OperationPage(self.driver).get_resource_count()
        print(a, b, c, d)
        print(e, f, g, h)
        self.assertEqual(int(e)-int(a), 1)
        self.assertEqual(int(f)-int(b), 1)
        self.assertEqual(int(g)-int(c), 1)
        self.assertEqual(int(h)-int(d), 0)

    def test_add_follow(self):
        OperationPage(self.driver).enter_operation_page()
        time.sleep(2)
        (a, b, c, d) = OperationPage(self.driver).get_resource_count()
        print(a,b,c,d)
        ResourceActionPage(self.driver).follow("111111111")
        time.sleep(2)
        (e, f, g, h) = OperationPage(self.driver).get_resource_count()
        print(e,f,g,h)
        self.assertEqual(int(e)-int(a), 0)
        self.assertEqual(int(f)-int(b), -1)
        self.assertEqual(int(g)-int(c), -1)
        self.assertEqual(int(h)-int(d), 0)

    def test_sign(self):
        pass







# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
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
        IndexPage(self.driver).add_depart_resource()

    def tearDown(self):
        self.driver.quit()

    def test_add_resource(self):
        resource_data = AddPage(self.driver).add_resource_data()
        print(resource_data)
        print(resource_data[0])

        AddPage(self.driver).add_resource(*resource_data)


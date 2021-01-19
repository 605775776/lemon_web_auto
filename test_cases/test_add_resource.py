# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.add_page import AddPage
from selenium import webdriver
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
        IndexPage(self.driver).add_my_resource()

    def tearDown(self):
        self.driver.quit()

    def test_add_resource(self):
        AddPage(self.driver)






# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from selenium import webdriver
from test_data import Global_Datas as GD
from test_data import login_datas as lds
import ddt



@ddt.ddt
class test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*lds.success)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        pass



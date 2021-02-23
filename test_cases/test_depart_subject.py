# coding:utf-8
# 2021/2/20 16:50
# Author:dsw

import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
from selenium import webdriver

from PageObjects.my_resource_page import MyResourcePage
from test_data import Global_Datas as GD
from test_data import login_datas as lds
from test_data import resource_generate as rg

import ddt


@ddt.ddt
class test_add_resource(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*lds.success)
        IndexPage(self.driver).entrance()
        IndexPage(self.driver).depart_resource()
        IndexPage(self.driver).depart_subject_depart()

    def tearDown(self):
        self.driver.quit()

    def test_add_resource(self):

        # 点击添加资源
        MyResourcePage(self.driver).add_resource()

        # 添加资源
        AddPage(self.driver).add_resource(*rg.data)

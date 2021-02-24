# coding:utf-8
# 2021/2/20 16:50
# Author:dsw
import time
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
from selenium import webdriver

from PageObjects.my_resource_page import MyResourcePage
from PageObjects.resource_action_page import ResourceActionPage
from test_data import Global_Datas as GD
from test_data import login_datas as lds
from test_data import resource_generate as rg

import ddt


@ddt.ddt
class test_add_resource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(GD.login_url)
        cls.driver.maximize_window()
        LoginPage(cls.driver).login(*lds.success)
        IndexPage(cls.driver).entrance()
        IndexPage(cls.driver).depart_resource()
        IndexPage(cls.driver).depart_subject_depart()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_resource(self):
        # 获取当前统计数据
        time.sleep(2)
        (a1, b1, c1) = MyResourcePage(self.driver).get_depart_count()

        # 点击添加资源
        MyResourcePage(self.driver).add_resource()

        # 添加资源
        AddPage(self.driver).add_resource(*rg.data)

        time.sleep(2)
        (a2, b2, c2) = MyResourcePage(self.driver).get_depart_count()

        print(a1, b1, c1)
        print(a2, b2, c2)

        self.assertEqual(int(a2) - int(a1), 1)
        self.assertEqual(int(b2) - int(b1), 0)
        self.assertEqual(int(c2) - int(c1), 1)


    def test_batch_allocate_branch(self):
        # 获取当前统计数据

        a, b, c = ResourceActionPage(self.driver).batch_allocate_branch()
        self.assertEqual(a, 0)
        self.assertEqual(b, 1)
        self.assertEqual(c, -1)


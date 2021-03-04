# coding:utf-8
# 2021/3/4 17:22
# Author:dsw

import time
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.ydy_page import YdyPage
from PageObjects.index_page import IndexPage
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
        IndexPage(self.driver).education_center()
        IndexPage(self.driver).course_product()
        IndexPage(self.driver).ydy_course()

    def tearDown(self):
        self.driver.quit()



    # 添加1对1课程
    def test_add_ydy_course(self):
        before_add_count = YdyPage(self.driver).course_count()
        res = YdyPage(self.driver).add_course()
        print(res)
        YdyPage(self.driver).return_button()
        after_add_count = YdyPage(self.driver).course_count()
        self.assertEqual(after_add_count-before_add_count, 1)




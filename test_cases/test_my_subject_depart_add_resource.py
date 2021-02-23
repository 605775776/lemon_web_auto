# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import time
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
from PageObjects.my_resource_page import MyResourcePage
from PageObjects.resource_action_page import ResourceActionPage

from selenium import webdriver
from test_data import Global_Datas as GD
from test_data import login_datas as lds
from test_data import resource_generate as rg

import ddt


@ddt.ddt
class test_add_resource(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*lds.success)
        IndexPage(self.driver).entrance()
        IndexPage(self.driver).my_resource()
        IndexPage(self.driver).my_subject_depart()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_add_resource(self):
        time.sleep(2)
        # 获取当前统计数据
        (a1, b1, c1, d1, e1) = MyResourcePage(self.driver).get_my_depart_count()

        # 点击添加资源
        MyResourcePage(self.driver).add_resource()

        # 添加资源
        AddPage(self.driver).add_resource(*rg.data)
        time.sleep(2)
        # 添加资源后统计数据
        (a2, b2, c2, d2, e2) = MyResourcePage(self.driver).get_my_depart_count()
        print(a1, b1, c1, d1, e1)
        print(a2, b2, c2, d2, e2)

        # 断言
        self.assertEqual(int(a2)-int(a1), 1)
        self.assertEqual(int(b2)-int(b1), 1)
        self.assertEqual(int(c2)-int(c1), 1)
        self.assertEqual(int(d2)-int(d1), 0)
        self.assertEqual(int(e2)-int(e1), 0)

    def test_allocate_branch(self):

        branch = IndexPage(self.driver).get_current_branch()
        ResourceActionPage(self.driver).click_allocate_branch()
        ResourceActionPage(self.driver).allocate_branch(branch)
        time.sleep(2)
        msg_success = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        print(msg_success)
        self.assertEqual(msg_success, "操作成功")
        ResourceActionPage(self.driver).click_allocate_branch()
        time.sleep(2)
        msg_fail = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        print(msg_fail)
        self.assertEqual(msg_fail, "资源已分配到校区，不允许再次分配")

        # ResourceActionPage(self.driver).click_allocate_branch()
        # time.sleep(2)
        # msg = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        # print(msg)
        # self.assertEqual(msg, "资源已分配到校区，不允许再次分配")





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
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(GD.login_url)
        cls.driver.maximize_window()
        LoginPage(cls.driver).login(*lds.success)
        IndexPage(cls.driver).switch_branch(1)
        time.sleep(2)
        IndexPage(cls.driver).entrance()
        IndexPage(cls.driver).my_resource()
        IndexPage(cls.driver).my_subject_depart()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 我的资源-学科部添加资源 添加资源及统计资源数据用例
    def test_01add_resource(self):
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

        # 断言
        self.assertEqual(a2 - a1, 1)
        self.assertEqual(b2 - b1, 1)
        self.assertEqual(c2 - c1, 1)
        self.assertEqual(d2 - d1, 0)
        self.assertEqual(e2 - e1, 0)

    #     # 我的资源-学科部添加资源 分配校区用例
    def test_allocate_branch(self):
        branch = IndexPage(self.driver).get_current_branch()
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

    # 我的资源-学科部 资源添加预约访数量统计
    def test_02add_appointment(self):
        # 获取当前统计数据
        time.sleep(2)
        (a1, b1, c1, d1, e1) = MyResourcePage(self.driver).get_my_depart_count()
        ResourceActionPage(self.driver).appointment(rg.data[0])

        # 添加预约访后统计数据
        time.sleep(2)
        (a2, b2, c2, d2, e2) = MyResourcePage(self.driver).get_my_depart_count()

        # 断言
        self.assertEqual(a2 - a1, 0)
        self.assertEqual(b2 - b1, 0)
        self.assertEqual(c2 - c1, 0)
        self.assertEqual(d2 - d1, 0)
        self.assertEqual(e2 - e1, 1)

    # 学科部分配到校区的资源进行分配校区归属人用例
    def test_allocate_branch_belonger(self):
        IndexPage(self.driver).branch_resource()
        time.sleep(1)

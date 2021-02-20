# coding:utf-8
# 2021/1/19 10:08
# Author:dsw
import time
import unittest
from lxml import etree
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
from PageObjects.operation_depart_page import OperationPage
from PageObjects.resource_action_page import ResourceActionPage
from selenium import webdriver
from test_data import Global_Datas as GD
from test_data import login_datas as lds
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
        IndexPage(self.driver).operation_depart()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_add_resource(self):
        time.sleep(2)
        # 获取当前统计数据
        (a, b, c, d) = OperationPage(self.driver).get_resource_count()

        # 创建资源信息
        resource_data = AddPage(self.driver).add_resource_data()

        # 点击添加资源
        OperationPage(self.driver).add_resource()

        # 添加资源
        AddPage(self.driver).add_resource(*resource_data)

        # 添加资源后统计数据
        (e, f, g, h) = OperationPage(self.driver).get_resource_count()
        print(a, b, c, d)
        print(e, f, g, h)

        # 断言
        self.assertEqual(int(e)-int(a), 1)
        self.assertEqual(int(f)-int(b), 1)
        self.assertEqual(int(g)-int(c), 1)
        self.assertEqual(int(h)-int(d), 0)

    def test_follow(self):

        time.sleep(2)
        # 获取当前统计数据
        (a, b, c, d) = OperationPage(self.driver).get_resource_count()

        # 添加跟进 最迟回访日期选择日期下个月1号

        ResourceActionPage(self.driver).follow("沟通内容")
        time.sleep(2)
        # 跟进操作后统计数据
        (e, f, g, h) = OperationPage(self.driver).get_resource_count()

        print(a, b, c, d)
        print(e, f, g, h)
        # 断言
        self.assertEqual(int(e)-int(a), 0)
        self.assertEqual(int(f)-int(b), -1)
        self.assertEqual(int(g)-int(c), -1)
        self.assertEqual(int(h)-int(d), 0)

    def test_appointment(self):
        # 获取当前统计数据
        time.sleep(2)
        (a, b, c, d) = OperationPage(self.driver).get_resource_count()
        ResourceActionPage(self.driver).appointment()

        # 跟进操作后统计数据
        time.sleep(2)
        (e, f, g, h) = OperationPage(self.driver).get_resource_count()

        # 断言
        self.assertEqual(int(e)-int(a), 0)
        self.assertEqual(int(f)-int(b), 0)
        self.assertEqual(int(g)-int(c), 0)
        self.assertEqual(int(h)-int(d), 1)
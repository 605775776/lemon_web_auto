# coding:utf-8
# 2021/3/18 9:28
# Author:dsw
import time
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.my_resource_add_page import AddPage
from PageObjects.my_resource_page import MyResourcePage
from PageObjects.depart_resource_page import DepartResourcePage
from PageObjects.resource_action_page import ResourceActionPage
from PageObjects.branch_resource_page import BranchPage
from test_data import Global_Datas as GD
from test_data import login_datas as lds
import ddt


@ddt.ddt
class test_add_resource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(GD.login_url)
        cls.driver.maximize_window()
        # 登录
        LoginPage(cls.driver).login(*lds.success)

        # 招生入口
        IndexPage(cls.driver).entrance()

        # 校区资源
        IndexPage(cls.driver).branch_resource()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # 我的资源-运营部添加资源-跟进 数量统计用例
    def test_add_resource(self):

        # 校区资源数量统计
        m1, m2, m3, m4 = BranchPage(self.driver).get_branch_resource_count()
        self.assertEqual(m1, m4)
        print(m1, m2, m3, m4)

        # 进入运营部 资源数量统计
        IndexPage(self.driver).enter_my_resource_operation_depart()
        p1, p2, p3, p4, p5 = MyResourcePage(self.driver).get_resource_count()
        self.assertEqual(p1, p5)
        print(p1, p2, p3, p4, p5)

        # 运营部添加资源 最迟回访时间为当天
        resource_data = AddPage(self.driver).add_resource_data()
        MyResourcePage(self.driver).add_resource()
        AddPage(self.driver).add_resource(*resource_data)

        # 运营部 资源数量统计
        q1, q2, q3, q4, q5 = MyResourcePage(self.driver).get_resource_count()
        self.assertEqual(q1, q5)

        # 添加资源前后断言
        self.assertEqual(q1 - p1, 1)
        self.assertEqual(q2 - p2, 1)
        self.assertEqual(q3 - p3, 1)
        self.assertEqual(q4 - p4, 0)
        self.assertEqual(q5 - p5, 1)











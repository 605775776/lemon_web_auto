# coding:utf-8
# 2021/2/20 16:50
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



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 部门资源-添加资源及资源数量统计用例
    def test_add_resource(self):

        # 我的资源-市场部资源数量统计
        IndexPage(self.driver).enter_my_resource_market_depart()
        (m1, m2, m3, m4, m5, m6, m7) = MyResourcePage(self.driver).get_my_depart_count()

        print(m1, m2, m3, m4, m5, m6, m7)
        self.assertEqual(m1, m7)

        IndexPage(self.driver).enter_depart_market_depart()
        # 部门资源-添加资源前资源数量统计
        time.sleep(2)
        (a1, b1, c1, d1) = DepartResourcePage(self.driver).get_depart_count()

        # 全部资源与右下角资源数量断言
        self.assertEqual(a1, d1)

        # 部门资源-添加资源
        resource_data = AddPage(self.driver).add_resource_data()
        MyResourcePage(self.driver).add_resource()
        AddPage(self.driver).add_resource(*resource_data)

        # 部门资源-添加资源后资源数量统计
        (a2, b2, c2, d2) = DepartResourcePage(self.driver).get_depart_count()

        # 资源数量断言
        self.assertEqual(a2 - a1, 1)
        self.assertEqual(b2 - b1, 0)
        self.assertEqual(c2 - c1, 1)
        self.assertEqual(d2 - d1, 1)

        # 我的资源-市场部资源数量统计
        IndexPage(self.driver).enter_my_resource_market_depart()
        (n1, n2, n3, n4, n5, n6, n7) = MyResourcePage(self.driver).get_my_depart_count()
        print(n1, n2, n3, n4, n5, n6, n7)
        self.assertEqual(n1-m1, 1)
        self.assertEqual(n2-m2, 1)
        self.assertEqual(n3-m3, 1)
        self.assertEqual(n4-m4, 0)
        self.assertEqual(n5-m5, 0)
        self.assertEqual(n6-m6, 0)
        self.assertEqual(n7-m7, 0)

    # 部门资源-分配校区及分配后被禁止操作用例
    def test_allocate_branch(self):
        # 获取当前校区
        branch = IndexPage(self.driver).get_current_branch()
        # 部门资源-市场部统计
        (a1, b1, c1, d1) = DepartResourcePage(self.driver).get_depart_count()
        # 分配资源
        ResourceActionPage(self.driver).allocate_branch(branch)
        time.sleep(2)

        # 分配成功-提示断言
        msg_success = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        self.assertEqual(msg_success, "操作成功")

        # 分配后 部门资源-市场部统计
        time.sleep(2)
        (a2, b2, c2, d2) = DepartResourcePage(self.driver).get_depart_count()

        # 分配前后，部门资源-市场部统计
        self.assertEqual(a2, a1)
        self.assertEqual(b2 - b1, 1)
        self.assertEqual(c2 - c1, -1)
        self.assertEqual(d1, d2)

        # 已分配校区的资源 分配操作失败 提示消息断言
        ResourceActionPage(self.driver).click_allocate_branch()
        allocate_branch_msg_fail = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        self.assertEqual(allocate_branch_msg_fail, "资源已分配到校区，不允许再次分配")

        # 已分配校区的资源 修改操作失败 提示消息断言
        ResourceActionPage(self.driver).modify()
        modify_msg_fail = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        self.assertEqual(modify_msg_fail, "资源已分配到校区，不允许修改")

        # 已分配校区的资源 删除操作失败 提示消息断言
        ResourceActionPage(self.driver).delete()
        delete_msg_fail = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        self.assertEqual(delete_msg_fail, "资源已分配到校区，不允许删除")

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
from PageObjects.branch_resource_page import BranchPage
from test_data import Global_Datas as GD
from test_data import login_datas as lds
import ddt


@ddt.ddt
class test_add_and_allocate_resource(unittest.TestCase):

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
    def test_01_add_resource(self):
        # 我的资源-市场部资源数量统计
        IndexPage(self.driver).enter_my_resource_market_depart()
        (m1, m2, m3, m4, m5, m6, m7) = MyResourcePage(self.driver).get_my_depart_count()
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

        # 已分配/未分配资源数量统计及断言
        DepartResourcePage(self.driver).switch_radio_to_unallocate()
        p1, p2, p3, p4 = DepartResourcePage(self.driver).get_depart_count()
        print(p1, p2, p3, p4)
        self.assertEqual(p3, p4)
        DepartResourcePage(self.driver).switch_radio_to_allocated()
        p1, p2, p3, p4 = DepartResourcePage(self.driver).get_depart_count()
        print(p1, p2, p3, p4)
        self.assertEqual(p1, p3 + p4)
        DepartResourcePage(self.driver).switch_radio_to_all()

        # 我的资源-市场部资源数量统计
        IndexPage(self.driver).my_market_depart()
        (n1, n2, n3, n4, n5, n6, n7) = MyResourcePage(self.driver).get_my_depart_count()

        # 部门资源添加资源后 我的资源市场部资源数量断言
        self.assertEqual(n1 - m1, 1)
        self.assertEqual(n2 - m2, 1)
        self.assertEqual(n3 - m3, 1)
        self.assertEqual(n4 - m4, 0)
        self.assertEqual(n5 - m5, 0)
        self.assertEqual(n6 - m6, 0)
        self.assertEqual(n7 - m7, 1)



    # 将新资源重新分配部门归属人 再分配回来
    def test_02_allocate_depart_belonger(self):

        # # 我的资源市场部统计
        (m1, m2, m3, m4, m5, m6, m7) = MyResourcePage(self.driver).get_my_depart_count()
        # 跳转到部门资源市场部
        IndexPage(self.driver).depart_market_depart()

        # 分配部门归属人 空白断言
        ResourceActionPage(self.driver).click_allocate_depart_belonger()
        ResourceActionPage(self.driver).click_confirm_button()
        tips = ResourceActionPage(self.driver).tips()
        self.assertEqual(tips, "请选择部门归属人")
        ResourceActionPage(self.driver).close_window()

        ResourceActionPage(self.driver).allocate_depart_belonger('wjq')

        # 跳转到我的资源市场部统计及断言
        IndexPage(self.driver).my_market_depart()
        (n1, n2, n3, n4, n5, n6, n7) = MyResourcePage(self.driver).get_my_depart_count()

        print(m1, m2, m3, m4, m5, m6, m7)
        print(n1, n2, n3, n4, n5, n6, n7)
        self.assertEqual(n1 - m1, -1)
        self.assertEqual(n2 - m2, -1)
        self.assertEqual(n3 - m3, -1)
        self.assertEqual(n4 - m4, 0)
        self.assertEqual(n5 - m5, 0)
        self.assertEqual(n6 - m6, 0)
        self.assertEqual(n7 - m7, -1)

        # 跳转到部门资源市场部 重新分配给我
        IndexPage(self.driver).depart_market_depart()
        ResourceActionPage(self.driver).allocate_depart_belonger('dswen')

    # 部门资源-分配校区及分配后被禁止操作用例
    def test_03_allocate_branch(self):

        # 进入我的资源-市场部
        IndexPage(self.driver).my_market_depart()
        # 获取当前校区
        branch = IndexPage(self.driver).get_current_branch()
        (m1, m2, m3, m4, m5, m6, m7) = MyResourcePage(self.driver).get_my_depart_count()
        IndexPage(self.driver).depart_market_depart()

        # 部门资源-市场部统计
        (a1, b1, c1, d1) = DepartResourcePage(self.driver).get_depart_count()

        # 校区资源统计
        IndexPage(self.driver).branch_resource()
        (p1, p2, p3, p4) = BranchPage(self.driver).get_branch_resource_count()
        self.assertEqual(p1, p4)

        IndexPage(self.driver).depart_market_depart()
        # 分配校区
        ResourceActionPage(self.driver).allocate_branch(branch)
        time.sleep(2)

        # 分配成功-提示断言
        msg_success = self.driver.find_element_by_xpath("//p[@class='el-message__content']").text
        self.assertEqual(msg_success, "操作成功")

        # 分配后 部门资源-市场部统计
        time.sleep(2)
        (a2, b2, c2, d2) = DepartResourcePage(self.driver).get_depart_count()
        
        DepartResourcePage(self.driver).switch_radio_to_unallocate()
        k1, k2, k3, k4 = DepartResourcePage(self.driver).get_depart_count()
        print(k1, k2, k3, k4)
        self.assertEqual(k3, k4)
        DepartResourcePage(self.driver).switch_radio_to_allocated()
        k1, k2, k3, k4 = DepartResourcePage(self.driver).get_depart_count()
        print(k1, k2, k3, k4)
        self.assertEqual(k1, k3 + k4)
        DepartResourcePage(self.driver).switch_radio_to_all()

        # 分配前后，部门资源-市场部数量断言
        self.assertEqual(a2, a1)
        self.assertEqual(b2 - b1, 1)
        self.assertEqual(c2 - c1, -1)
        self.assertEqual(d1, d2)

        # 已分配校区的资源 分配操作失败 提示消息断言
        ResourceActionPage(self.driver).click_allocate_branch()
        time.sleep(1)
        allocate_branch_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(allocate_branch_msg, "资源已分配到校区，不允许再次分配")

        # 已分配校区的资源 修改操作失败 提示消息断言
        ResourceActionPage(self.driver).modify()
        time.sleep(1)
        modify_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(modify_msg, "资源已分配给校区，不允许修改")

        # 已分配校区的资源 删除操作失败 提示消息断言
        ResourceActionPage(self.driver).delete()
        time.sleep(1)
        delete_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(delete_msg, "资源已分配给校区，不允许删除")

        # 分配后 我的资源-市场部资源数量统计
        IndexPage(self.driver).my_market_depart()
        (n1, n2, n3, n4, n5, n6, n7) = MyResourcePage(self.driver).get_my_depart_count()

        # 部门资源分配资源后 我的资源市场部资源数量断言
        self.assertEqual(n1 - m1, 0)
        self.assertEqual(n2 - m2, 0)
        self.assertEqual(n3 - m3, 0)
        self.assertEqual(n4 - m4, 0)
        self.assertEqual(n5 - m5, 0)
        self.assertEqual(n6 - m6, 1)
        self.assertEqual(n7 - m7, 0)

        # 分配后 校区资源数量统计
        IndexPage(self.driver).branch_resource()
        (q1, q2, q3, q4) = BranchPage(self.driver).get_branch_resource_count()

        # 分配后 校区资源数量断言
        self.assertEqual(q1 - p1, 1)
        self.assertEqual(q2 - p2, 0)
        self.assertEqual(q3 - p3, 1)
        self.assertEqual(q4 - p4, 1)
        self.assertEqual(q1, q4)

    # 将市场部分给校区的资源分配校区归属人
    def test_04_allocate_branch_belonger(self):
        # 分配校区归属人前 校区资源统计
        a1, b1, c1, d1 = BranchPage(self.driver).get_branch_resource_count()
        print(a1, b1, c1, d1)

        # 分配校区归属人前 部门资源-市场部统计
        IndexPage(self.driver).depart_market_depart()
        m1, m2, m3, m4 = DepartResourcePage(self.driver).get_depart_count()
        print(m1, m2, m3, m4)

        # 分配校区归属人前 我的资源-市场部统计
        IndexPage(self.driver).my_market_depart()
        p1, p2, p3, p4, p5, p6, p7 = MyResourcePage(self.driver).get_my_depart_count()
        print(p1, p2, p3, p4, p5, p6, p7)

        # 分配校区归属人前 我的资源-运营部统计
        IndexPage(self.driver).operation_depart()
        x1, x2, x3, x4, x5 = MyResourcePage(self.driver).get_resource_count()
        print(x1, x2, x3, x4, x5)


        # 修改断言
        IndexPage(self.driver).branch_resource()
        ResourceActionPage(self.driver).branch_modify_resource()
        modify_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(modify_msg, "请分配校区归属人再修改!")

        # 分配校区归属人操作
        ResourceActionPage(self.driver).click_allocate_branch_belonger()
        ResourceActionPage(self.driver).click_confirm_button()
        tips = ResourceActionPage(self.driver).tips()
        self.assertEqual('请选择校区归属人', tips)

        ResourceActionPage(self.driver).close_window()
        ResourceActionPage(self.driver).allocate_branch_belonger('dswen')
        allocate_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(allocate_msg, "分配成功!")

        # 分配校区归属人后 校区资源统计
        a2, b2, c2, d2 = BranchPage(self.driver).get_branch_resource_count()
        print(a2, b2, c2, d2)

        self.assertEqual(a2, a1)
        self.assertEqual(b2 - b1, 1)
        self.assertEqual(c2 - c1, -1)
        self.assertEqual(d2, d1)

        # 分配校区归属人后 部门资源-市场部统计及断言
        IndexPage(self.driver).depart_market_depart()
        n1, n2, n3, n4 = DepartResourcePage(self.driver).get_depart_count()
        print(n1, n2, n3, n4)

        self.assertEqual(n1, m1)
        self.assertEqual(n2 - m2, -1)
        self.assertEqual(n3, m3)
        self.assertEqual(n4, m4)

        # 分配校区归属人后 我的资源-市场部统计及断言
        IndexPage(self.driver).my_market_depart()
        q1, q2, q3, q4, q5, q6, q7 = MyResourcePage(self.driver).get_my_depart_count()
        print(q1, q2, q3, q4, q5, q6, q7)

        self.assertEqual(q1, p1)
        self.assertEqual(q2, p2)
        self.assertEqual(q3, p3)
        self.assertEqual(q4 - p4, 1)
        self.assertEqual(q5, p5)
        self.assertEqual(q6 - p6, -1)
        self.assertEqual(q7, p7)

        # 分配校区归属人后 我的资源-运营部统计
        IndexPage(self.driver).operation_depart()
        y1, y2, y3, y4, y5 = MyResourcePage(self.driver).get_resource_count()
        print(y1, y2, y3, y4, y5)

        self.assertEqual(y1 - x1, 1)
        self.assertEqual(y2 - x2, 1)
        self.assertEqual(y3 - x3, 1)
        self.assertEqual(y4, x4)
        self.assertEqual(y5 - x5, 1)

        # 分配校区归属人更新最迟回访时间
        IndexPage(self.driver).branch_resource()
        ResourceActionPage(self.driver).allocate_branch_belonger('dswen', 1)
        allocate_msg = ResourceActionPage(self.driver).msg()
        self.assertEqual(allocate_msg, "分配成功!")

        # 分配校区归属人后 校区资源统计
        a3, b3, c3, d3 = BranchPage(self.driver).get_branch_resource_count()
        print(a3, b3, c3, d3)

        self.assertEqual(b3 - b2, -1)

        # 分配校区归属人后 我的资源-市场部统计
        IndexPage(self.driver).my_market_depart()
        li_depart_count = MyResourcePage(self.driver).get_my_depart_count()
        print(li_depart_count[3])
        self.assertEqual(q4 - li_depart_count[3], 1)

        # 分配校区归属人前 我的资源-运营部统计
        IndexPage(self.driver).operation_depart()
        li_operation_count = MyResourcePage(self.driver).get_resource_count()
        self.assertEqual(y3 - li_operation_count[2], 1)



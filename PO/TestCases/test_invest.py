import unittest
from selenium import webdriver
from PO.TestDatas import Global_Datas as GD
from PO.PageObjects.login_page import LoginPage as lp
from PO.PageObjects.bid_page import BidPage
from PO.PageObjects.index_page import IndexPage as ip
from PO.PageObjects.user_page import UserPage




class TestInvest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()

        # 登录
        lp(self.driver).login(*GD.user_invest)

    def tearDown(self):
        self.driver.quit()


    # 投资成功2000 看余额变化及标的变化
    def test_invest_success(self):
        ip(self.driver).click_first_bid()
        bp = BidPage(self.driver)
        user_money_before_invest = bp.get_user_money()
        bid_money_before_invest = bp.get_bid_money()
        bp.invest(2000)
        bp.click_success_button()


        # 个人页面
        user_money_after_invest = UserPage(self.driver).get_user_money()
        print(user_money_before_invest)
        user_money_compare = int(float(user_money_before_invest) - float(user_money_after_invest))
        self.assertEqual(user_money_compare, 2000)
        self.driver.back()
        self.driver.refresh()
        bid_money_after_invest = bp.get_bid_money()
        bid_money_compare = int(float(bid_money_before_invest) - float(bid_money_after_invest))
        self.assertEqual(bid_money_compare, 2000)

        """ 
        首页 选标
        标页面 获取金额
        输入2000 投标
        标页面投标成功 点击 按钮
        1、是否少了2000
        2、标的余额是否少了2000
        
        """

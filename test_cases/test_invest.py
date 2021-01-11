import unittest
from selenium import webdriver
from test_data import Global_Datas as GD
from PageObjects.login_page import LoginPage as lp
from PageObjects.bid_page import BidPage
from PageObjects.index_page import IndexPage as ip
from PageObjects.user_page import UserPage


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
        ip(self.driver).click_second_bid()
        bid_money = 8000
        bp = BidPage(self.driver)
        user_money_before_invest = bp.get_user_money()
        bid_money_before_invest = bp.get_bid_money()
        bp.invest(bid_money)
        bp.click_success_button()


        # 个人页面
        user_money_after_invest = UserPage(self.driver).get_user_money()
        user_money_compare = int(float(user_money_before_invest) - float(user_money_after_invest))
        self.assertEqual(user_money_compare, bid_money)
        self.driver.back()
        self.driver.refresh()
        bid_money_after_invest = bp.get_bid_money()
        bid_money_compare = int(float(bid_money_before_invest) - float(bid_money_after_invest))
        self.assertEqual(bid_money_compare, bid_money)

    def test_invest_failed_01(self):
        ip(self.driver).click_second_bid()
        bp = BidPage(self.driver)
        user_money_before_invest = bp.get_user_money()
        bid_money_before_invest = bp.get_bid_money()


        bid_money = (int(float(user_money_before_invest)))*100
        bp.invest(bid_money)
        self.assertEqual(bp.invest_failed_01(), "投标金额大于可用金额")


    def test_invest_failed_02(self):
        ip(self.driver).click_third_bid()
        bp = BidPage(self.driver)
        bid_money_before_invest = bp.get_bid_money()
        print(bid_money_before_invest)
        bid_money = (int(float(bid_money_before_invest))+1) * 10000
        print(bid_money)
        bp.invest(bid_money)
        self.assertEqual(bp.invest_failed_02(), "购买标的金额不能大于标总金额")




        """ 
        首页 选标
        标页面 获取金额
        输入2000 投标
        标页面投标成功 点击 按钮
        1、是否少了2000
        2、标的余额是否少了2000
        
        """

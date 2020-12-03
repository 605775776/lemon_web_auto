import unittest
from selenium import webdriver
from PO.TestDatas import Global_Datas as GD
from PO.PageObjects.login_page import LoginPage as lp




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
        pass

        """
        首页 选标
        标页面 获取金额
        输入2000 投标
        标页面投标成功 点击 按钮
        1、是否少了2000
        2、标的余额是否少了2000
        
        """

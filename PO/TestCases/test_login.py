import unittest
from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.index_page import IndexPage
from selenium import webdriver
from PO.TestDatas import Global_Datas as GD
from PO.TestDatas import login_datas as lds
import time
import ddt


@ddt.ddt
class test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        LoginPage(self.driver).login(*lds.success)
        time.sleep(3)
        self.assertTrue(IndexPage(self.driver).get_element_exists())


    @ddt.data(*lds.cases)
    def test_login_failed(self, case):
        lp = LoginPage(self.driver)
        lp.login(case['user'], case['password'])
        self.assertEqual(lp.msg_from_login_form(), case['check'])

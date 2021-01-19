import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from selenium import webdriver
from test_data import Global_Datas as GD
from test_data import login_datas as lds
import time
import ddt
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@ddt.ddt
class test_login(unittest.TestCase):

    def setUp(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        LoginPage(self.driver).login(*lds.success)




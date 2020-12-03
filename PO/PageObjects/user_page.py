from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc


class BidPage:

    def __init__(self, driver:WebDriver):
        self.driver = driver
    # 获取用户余额
    def get_user_money(self):
        pass




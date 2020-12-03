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



    # 一个函数执行一个功能 方便后续调用
    # 获取标的余额
    def get_bid_money(self):
        pass
    # 输入金额2000 点投标
    def invest(self, money):
        pass

    # 投标成功 点击查看并激活按钮
    def click_success_button(self):
        pass

    # 点击第二个标去投资
    def click_first_bid(self):
        pass
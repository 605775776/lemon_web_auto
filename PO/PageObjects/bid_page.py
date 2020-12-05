from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc
from PO.PageLocators.bid_page_locs import BidPageLocs as loc


class BidPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 一个函数执行一个功能 方便后续调用
    # 获取标的余额
    def get_bid_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.bid_money_text))
        return self.driver.find_element(*loc.bid_money_text).text

    # 输入金额2000 并投标
    def invest(self, invest_money):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.money_input))
        self.driver.find_element(*loc.money_input).send_keys(invest_money)
        self.driver.find_element(*loc.invest_button).click()

    # 投标成功 点击查看并激活按钮
    def click_success_button(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.active_button_on_successPop))
        self.driver.find_element(*loc.active_button_on_successPop).click()

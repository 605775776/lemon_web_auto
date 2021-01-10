from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc
from PO.PageLocators.bid_page_locs import BidPageLocs as loc
from PO.Common.basepage import BasePage

class BidPage(BasePage):

    # 获取用户余额
    def get_user_money(self):
        return self.get_ele_attribute(loc.money_input, "data-amount", "标页面-获取用户投资余额")
    # 一个函数执行一个功能 方便后续调用
    # 获取标的余额

    def get_bid_money(self):
        return self.get_ele_text(loc.bid_money_text, "标页面-获取标的可投余额")

    # 输入金额   并投标
    def invest(self, invest_money):

        self.input_text(loc.money_input, invest_money, "标页面-输入投资的金额")
        self.click_element(loc.invest_button, "标页面-点击投标")

    # 投标成功 点击查看并激活按钮
    def click_success_button(self):
        self.click_element(loc.active_button_on_successPop, "标页面-点击查看并激活按钮")





    # # 投标失败1 输入金额大于用户金额 弹出信息
    # def invest_failed_01(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_failed))
    #     return self.driver.find_element(*loc.invest_failed).text
    #
    #
    # # 投资失败2 投标金额大于标的可投金额 弹出信息
    # def invest_failed_02(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_failed))
    #     return self.driver.find_element(*loc.invest_failed).text

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    bp = BasePage(driver)
    search_loc = ("id", "kw")
    button_loc = ("id", "su")
    bp.input_text(search_loc, "柠檬班", "百度输入操作" )
    bp.click_element(button_loc, "百度页面-点击百度一下")
    driver.quit()
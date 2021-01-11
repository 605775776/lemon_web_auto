
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc
from PO.Common.basepage import BasePage

class IndexPage(BasePage):


    # 是否存在元素  True/False
    def get_element_exists(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.exit_link))
            # return True
        except:
            return False

        else:
            return True

    # 点击第1个标去投资
    def click_first_bid(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button).click()

    # 点击第2个标去投资
    def click_second_bid(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button_2).click()

    # 点击第3个标去投资
    def click_third_bid(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button_3).click()

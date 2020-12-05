from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc
from PO.PageLocators.user_page_locs import UserPageLocs as loc


class UserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.user_leftMoney))
        return self.driver.find_element(*loc.user_leftMoney).text.strip("元")

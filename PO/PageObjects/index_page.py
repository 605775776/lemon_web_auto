from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.PageLocators.index_page_locs import IndexPageLocs as loc


class IndexPage:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 是否存在元素  True/False
    def get_element_exists(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.exit_link))
            # return True
        except:
            return False

        else:
            return True


from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    # # 获取元素-招生入口
    def get_element_entrance(self):
        self.wait_ele_visible(loc.entrance, ("CRM首页-招生入口", 'entrance'))



    #
    # def get_element(self, loc, img_name):
    #     pass
    # def get_element_exists(self):
    #     pass
    #     # try:
    #     #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.exit_link))
    #     #     # return True
    #     # except:
    #     #     return False
    #     #
    #     # else:
    #     #     return True
    #
    # # 点击第1个标去投资
    # def click_first_bid(self):
    #     self.click_element(loc.bid_button, "首页-点击第一个标投资按钮")
    # # 点击第2个标去投资
    # def click_second_bid(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.bid_button))
    #     self.driver.find_element(*loc.bid_button_2).click()
    #     self.click_element(loc.bid_button, "首页-点击第一个标投资按钮")
    # # 点击第3个标去投资
    # def click_third_bid(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.bid_button))
    #     self.driver.find_element(*loc.bid_button_3).click()

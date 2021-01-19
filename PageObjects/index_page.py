from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):


    # 我的资源-添加资源
    def add_my_resource(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))
        self.click_element(loc.my_resource, ("首页-点击我的资源", "my_resource"))
        self.click_element(loc.add_resource, ("首页-添加资源", "add_resource"))



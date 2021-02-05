from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):



    # 我的资源-添加资源
    def add_my_resource(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))
        self.click_element(loc.my_resource, ("首页-点击我的资源", "my_resource"))
        self.click_element(loc.add_resource, ("首页-添加资源", "add_resource"))

    # 部门资源-添加资源
    def add_depart_resource(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))
        self.click_element(loc.department_resource, ("首页-点击部门资源", "department_resource"))
        self.click_element(loc.add_resource, ("首页-添加资源", "add_resource"))

    # 校区资源-添加资源
    def add_branch_resource(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))
        self.click_element(loc.branch_resource, ("首页-点击校区资源", "branch_resource"))
        self.click_element(loc.add_resource, ("首页-添加资源", "add_resource"))

    # 我的资源-统计数据
    def find_resource_count(self):
        self.get_ele_text()



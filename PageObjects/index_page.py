from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    # 招生入口
    def entrance(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))

    # 招生入口-我的资源
    def my_resource(self):
        self.click_element(loc.my_resource, ("首页-点击我的资源", "my_resource"))

    # 我的资源-运营部页面
    def operation_depart(self):
        self.click_element(loc.operation_depart, ("首页-点击运营部", 'operation_depart'))

    # 我的资源-学科部页面
    def my_subject_depart(self):
        self.click_element(loc.my_subject_depart, ("首页-点击学科部", 'my_subject_depart'))

    # 我的资源-市场部页面
    def my_market_depart(self):
        self.click_element(loc.my_market_depart, ("首页-点击市场部", 'my_market_depart'))

    # 部门资源
    def depart_resource(self):
        self.click_element(loc.depart_resource, ("首页-点击部门资源", "department_resource"))

    # 部门资源-学科部
    def depart_subject_depart(self):
        self.click_element(loc.depart_subject, ("首页-部门资源-学科部", 'depart_subject'))

    # 部门资源-市场部
    def depart_market_depart(self):
        self.click_element(loc.depart_market, ("首页-部门资源-市场部", 'market_depart'))

    # 校区资源
    def branch_resource(self):
        self.click_element(loc.branch_resource, ("首页-点击校区资源", "branch_resource"))

    def get_current_branch(self):
        branch = self.get_ele_text(loc.branch, ("获取右上角校区", 'branch'))
        return branch


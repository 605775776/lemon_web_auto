import time

from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):

    # 招生入口
    def entrance(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))

    # 招生入口-我的资源
    def my_resource(self):
        self.click_element(loc.my_resource, ("首页-点击我的资源", "my_resource"))
        time.sleep(1)

    # 我的资源-运营部页面
    def operation_depart(self):
        self.click_element(loc.operation_depart, ("首页-点击运营部", 'operation_depart'))
        time.sleep(1)

    # 我的资源-学科部页面
    def my_subject_depart(self):
        self.click_element(loc.my_subject_depart, ("首页-点击学科部", 'my_subject_depart'))
        time.sleep(1)

    # 我的资源-市场部页面
    def my_market_depart(self):
        self.click_element(loc.my_market_depart, ("首页-点击市场部", 'my_market_depart'))
        time.sleep(2)

    # 部门资源
    def depart_resource(self):
        self.click_element(loc.depart_resource, ("首页-点击部门资源", "department_resource"))
        time.sleep(2)

    # 部门资源-学科部
    def depart_subject_depart(self):
        self.click_element(loc.depart_subject, ("首页-部门资源-学科部", 'depart_subject'))
        time.sleep(1)

    # 部门资源-市场部
    def depart_market_depart(self):
        self.click_element(loc.depart_market, ("首页-部门资源-市场部", 'market_depart'))
        time.sleep(1)

    # 校区资源
    def branch_resource(self):
        self.click_element(loc.branch_resource, ("首页-点击校区资源", "branch_resource"))
        time.sleep(1)

    # 进入我的资源运营部
    def enter_my_resource_operation_depart(self):
        self.my_resource()
        self.operation_depart()
        time.sleep(1)


    # 进入我的资源学科部
    def enter_my_resource_subject_depart(self):
        self.my_resource()
        self.my_subject_depart()
        time.sleep(1)


    # 进入我的资源市场部
    def enter_my_resource_market_depart(self):
        self.my_resource()
        self.my_market_depart()
        time.sleep(1)

    # 进入部门资源-学科部
    def enter_depart_subject_depart(self):
        self.depart_resource()
        self.depart_subject_depart()
        time.sleep(1)

    # 进入部门资源-市场部
    def enter_depart_market_depart(self):
        self.depart_resource()
        self.depart_market_depart()
        time.sleep(1)

    # 获取当前所在校区
    def get_current_branch(self):
        branch = self.get_ele_text(loc.branch, ("获取右上角校区", 'branch'))
        return branch

    # 教务中心
    def education_center(self):
        self.click_element(loc.education_center, ("首页-点击教务中心", 'education_center'))

    # 课程商品
    def course_product(self):
        self.click_element(loc.course_product, ("首页-点击课程管理", 'course_product'))

    # 1对1课程
    def ydy_course(self):
        self.click_element(loc.one_to_one_course, ("首页-点击1对1课程", 'one_to_one_course'))

    # 1对多课程
    def ydd_course(self):
        self.click_element(loc.one_to_many_course, ("首页-点击1对多课程", 'one_to_many_course'))

    # 切换校区
    def switch_branch(self, type):
        self.click_element(loc.switch_branch, ("首页-切换校区", 'switch_branch'))
        try:
            if type == 1:
                self.click_element(loc.gexinghua_branch, ("切换到个性化校区", 'gexinghua_branch'))
            elif type == 2:
                self.click_element(loc.jiayin_branch, ("切换到个性化校区", 'jiayin_branch'))
            elif type == 3:
                self.click_element(loc.peiying_branch, ("切换到个性化校区", 'peiying_branch'))
        except:
            raise Exception

# coding:utf-8
# 2021/2/5 15:50
# Author:dsw


from Common.basepage import BasePage
from PageLocators.operation_depart_page_locs import OperationDepartPageLocs as loc
from PageLocators.resource_detail_page_locs import ResourceDetailPageLocs as rloc

class ResourceActionPage(BasePage):


    def resource_detail_(self,tabNo):
        self.click_element(loc.first_resource_detail, ("运营部首页-第一个资源详情", 'first_resource_detail'))
        if tabNo == 1:
            self.click_element(rloc.base_info, ("资源详情页面-基本信息", 'base_info'))
        elif tabNo == 2:
            self.click_element(rloc.follow_info, ("资源详情页面-基本信息", 'follow_info'))
        elif tabNo == 3:
            self.click_element(rloc.appoint_info, ("资源详情页面-基本信息", 'appoint_info'))
        elif tabNo ==4:
            self.click_element(rloc.contact_info, ("资源详情页面-基本信息", 'contact_info'))
        elif tabNo == 5:
            self.click_element(rloc.listen_info, ("资源详情页面-基本信息", 'listen_info'))
        elif tabNo == 6:
            self.click_element(rloc.order_info, ("资源详情页面-基本信息", 'order_info'))


    def follow(self):
        self.click_element()
        self.click_element()

    def sign(self):
        pass

    def listen(self):
        pass

    def modify(self):
        pass

    def appointment(self):
        pass



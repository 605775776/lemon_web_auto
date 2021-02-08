# coding:utf-8
# 2021/2/5 15:50
# Author:dsw


from Common.basepage import BasePage
from PageLocators.operation_depart_page_locs import OperationDepartPageLocs as loc
from PageLocators.resource_detail_page_locs import ResourceDetailPageLocs as rloc
from PageLocators.follow_page_locs import FollowPageLocs as floc

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


    def follow(self,context):
        self.click_element(loc.first_resource_follow, ("运营部首页-点击第一个资源跟进", 'first_resource_follow'))
        self.click_element(floc.follow_method, ("跟进页面-选择跟进方式", 'follow_method'))
        self.click_element(floc.follow_method_weixin, ("跟进页面-选择微信/qq", 'follow_method_weixin'))
        self.click_element(floc.resource_progress, ("跟进页面-点击资源进展", 'resource_progress'))
        self.click_element(floc.progress_phoned, ("跟进页面-资源进展选择已回电", 'progresss_phoned'))
        self.click_element(floc.resource_stars, ("跟进页面-资源质量4颗星", 'resource_stars'))


        # self.click_element(floc.first_visit_date, ("跟进页面-首次上门日期为空时点击", 'first_visit_date'))
        # self.click_element(floc.first_visit_date_today, ("跟进页面-首次上门日期为空时点击", 'first_visit_date_today'))


        self.input_text(floc.communicate_context, context, ("跟进页面-填写沟通内容", 'communicate_context'))
        self.click_element(floc.next_follow_update, ("跟进页面-点击最迟回访日期", 'next_follow_update'))
        self.click_element(floc.next_month, ("跟进页面-选择最迟回访日期下一个月", 'next_month'))
        self.click_element(floc.next_month_1, ("跟进页面-选择最迟回访日期下一个月1号", 'next_month_1'))

        self.click_element(floc.confirm_button, ("跟进页面-确定", 'confirm_button'))

    def sign(self):
        self.click_element(loc.first_resource_sign, ("运营部首页-点击第一个资源签约", 'first_resource_sign'))


    def listen(self):
        pass

    def modify(self):
        pass

    def appointment(self):
        pass



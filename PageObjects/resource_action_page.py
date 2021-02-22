# coding:utf-8
# 2021/2/5 15:50
# Author:dsw


from Common.basepage import BasePage
from PageLocators.operation_depart_page_locs import OperationDepartPageLocs as loc
from PageLocators.resource_detail_page_locs import ResourceDetailPageLocs as rloc
from PageLocators.follow_page_locs import FollowPageLocs as floc
from PageLocators.add_appointment_page_locs import AddAppointmentPageLocs as aloc


class ResourceActionPage(BasePage):

    def resource_detail(self, tabNo):
        self.click_element(loc.first_resource_detail, ("运营部首页-第一个资源详情", 'first_resource_detail'))
        if tabNo == 1:
            self.click_element(rloc.base_info, ("资源详情页面-基本信息", 'base_info'))
        elif tabNo == 2:
            self.click_element(rloc.follow_info, ("资源详情页面-基本信息", 'follow_info'))
        elif tabNo == 3:
            self.click_element(rloc.appoint_info, ("资源详情页面-基本信息", 'appoint_info'))
        elif tabNo == 4:
            self.click_element(rloc.contact_info, ("资源详情页面-基本信息", 'contact_info'))
        elif tabNo == 5:
            self.click_element(rloc.listen_info, ("资源详情页面-基本信息", 'listen_info'))
        elif tabNo == 6:
            self.click_element(rloc.order_info, ("资源详情页面-基本信息", 'order_info'))

    def follow(self, context):
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
        self.click_element(floc.date_next_month, ("跟进页面-选择最迟回访日期下一个月", 'date_next_month'))
        self.click_element(floc.date_first_day, ("跟进页面-选择最迟回访日期下一个月1号", 'date_first_day'))

        self.click_element(floc.confirm, ("跟进页面-确定", 'confirm_button'))

    def sign(self):
        self.click_element(loc.first_resource_sign, ("运营部首页-点击第一个资源签约", 'first_resource_sign'))

    def listen(self):
        pass

    def modify(self):
        pass

    def appointment(self, appointment_object):
        # appointment_object_1 = self.driver.find_element_by_xpath("//td/div").text
        # appointment_object = self.get_ele_text(aloc.appointment_object_first_contact_name, ("获取列表第一个资源作为约访对象", 'appointment_object'))

        self.click_element(loc.first_resource_appointment, ("运营部首页-点击第一个资源的预约访元素", 'first_resource_appointment'))
        self.click_element(aloc.appointment_school, ("预约访页面-约访地点元素", 'appointment_school'))
        self.click_element(aloc.appointment_school_selected, ("预约访页面-默认选中第一个校区", 'appointment_school_selected'))
        self.input_text(aloc.appointment_object, appointment_object,
                        ("选中约访对象", 'appointment_object_selected'))
        self.click_element(aloc.appointment_date, ("预约日期元素定位", 'appointment_date'))
        self.click_element(aloc.date_next_month, ("选择下个月元素", 'date_next_month'))
        self.click_element(aloc.date_first_day, ("选择下个月1号", 'date_first_day'))
        self.click_element(aloc.appointment_time, ("选择预约时间-默认10点", 'appointment_time'))
        self.click_element(aloc.time_confirm, ("确认预约时间", 'time_confirm'))
        self.click_element(aloc.difficulty_list_2, ("2", '2'))
        self.click_element(aloc.difficulty_list_3, ("3", '3'))
        self.click_element(aloc.difficulty_list_4, ("4", '4'))
        self.click_element(aloc.difficulty_list_5, ("5", '5'))
        self.click_element(aloc.difficulty_list_6, ("6", '6'))
        self.click_element(aloc.difficulty_list_7, ("7", '7'))
        self.click_element(aloc.difficulty_list_8, ("8", '8'))
        self.click_element(aloc.difficulty_list_9, ("9", '9'))
        self.click_element(aloc.other_support, ("需求支持选择其他", 'other_support'))
        self.input_text(aloc.custom_support, "需要优惠支持", ("自定义需求支持", 'custom_support'))
        self.input_text(aloc.remark, "补充说明", ("填写补充说明", 'remark'))
        self.click_element(aloc.confirm, ("预约访页面-确定按钮", 'confirm'))

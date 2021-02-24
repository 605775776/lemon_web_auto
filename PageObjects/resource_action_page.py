# coding:utf-8
# 2021/2/5 15:50
# Author:dsw
import time

from Common.basepage import BasePage
from PageLocators.my_resource_page_locs import MyResourcePageLocs as mloc
from PageLocators.resource_detail_page_locs import ResourceDetailPageLocs as rloc
from PageLocators.follow_page_locs import FollowPageLocs as floc
from PageLocators.add_appointment_page_locs import AddAppointmentPageLocs as aloc
from PageLocators.allocate_page_locs import AllocatePageLocs as alloc
from PageLocators.depart_page_locs import DepartPageLocs as dloc
from PageLocators.index_page_locs import IndexPageLocs as iloc


class ResourceActionPage(BasePage):


    def resource_detail(self, tabNo):
        self.click_element(mloc.first_resource_detail, ("运营部首页-第一个资源详情", 'first_resource_detail'))
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

    # 资源跟进
    def follow(self, context):
        self.click_element(mloc.first_resource_follow, ("运营部首页-点击第一个资源跟进", 'first_resource_follow'))
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

    # 资源签约
    def sign(self):
        self.click_element(mloc.first_resource_sign, ("运营部首页-点击第一个资源签约", 'first_resource_sign'))

    # 资源试听
    def listen(self):
        pass

    # 修改资源
    def modify(self):
        pass

    # 添加预约访
    def appointment(self, appointment_object):

        self.click_element(mloc.depart_first_resource_appointment, ("运营部首页-点击第一个资源的预约访元素", 'first_resource_appointment'))
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



    def allocate_branch(self, branch):

        self.input_text(alloc.input_branch, branch, ("分配校区页面-归属校区输入", 'input_branch'))
        self.click_element(alloc.selected_branch, ("分配校区页面-点击返回列表元素", 'selected_branch'))
        self.click_element(alloc.confirm_button, ("分配校区页面-确认按钮", 'confirm_button'))

    def click_allocate_branch(self):
        self.click_element(mloc.first_resource_allocate_branch, ("资源列表-点击第一个资源分配校区", 'first_resource_allocate_branch'))
    def click_modify_resource(self):
        self.click_element(dloc.allocate_branch)


    def batch_allocate_branch(self):
        time.sleep(2)
        a1, b1, c1 = self.get_depart_count()
        self.click_element(dloc.checkbox_selected, ("资源列表-点击第一个资源的checkbox", 'checkbox_selected'))
        self.click_element(dloc.batch_allocate_branch, ("批量分配校区", 'batch_allocate_branch'))
        branch = self.get_ele_text(iloc.branch, ("获取右上角校区", 'branch'))
        self.input_text(alloc.input_branch, branch, ("输入右上角校区", 'input_branch'))
        self.click_element(alloc.selected_branch, ("点击下拉列表返回校区", 'selected_branch'))
        self.click_element(alloc.confirm_button, ("点击确认按钮", 'confirm_button'))
        time.sleep(2)
        a2, b2, c2 = self.get_depart_count()
        return int(a2)-int(a1), int(b2)-int(b1), int(c2)-int(c1)

    # 部门资源-学科部/市场部统计
    def get_depart_count(self):
        all_resource_count = self.get_ele_text(dloc.all_resource_count, ("学科部/市场部-全部资源统计", "all_resource_count"))
        has_allocated_to_be_process_count = self.get_ele_text(dloc.allocated_to_be_process_count,
                                                              ("学科部/市场部-已分配待处理统计", "allocated_to_be_process_count"))
        unallocated_branch_resource_count = self.get_ele_text(dloc.unallocated_count,
                                                              ("学科部/市场部-未分配校区资源统计", 'unallocated_count'))

        return all_resource_count, has_allocated_to_be_process_count, unallocated_branch_resource_count




        # wait_allocate_resource_count = int((self.get_ele_text(alloc.wait_allocate_resource_count_str, ("待分配资源数量", 'wait_allocate_resource_count_str')))[0])
        # allocated_resource_count = int(self.get_ele_text(alloc.allocated_resource_count_str, ("已分配资源数量统计", 'allocated_resource_count_str'))[0])
        # a = int((self.get_ele_text(alloc.selected_resource_count, ("已选资源数量统计", 'selected_resource_count')))[2: -11])
        #
        # print(wait_allocate_resource_count)
        # print(allocated_resource_count)
        # print(a)
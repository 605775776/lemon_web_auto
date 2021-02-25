# coding:utf-8
# 2021/2/5 10:52
# Author:dsw

from PageLocators.my_resource_page_locs import MyResourcePageLocs as mloc
from PageLocators.index_page_locs import IndexPageLocs as iloc
from PageLocators.depart_page_locs import DepartPageLocs as dloc
from Common.basepage import BasePage


class MyResourcePage(BasePage):

    def add_resource(self):
        self.click_element(mloc.add_resource, ("首页-添加资源", "add_resource"))

    # 我的资源-运营部统计
    def get_resource_count(self):
        all_resource_count = self.get_ele_text(mloc.all_resource_count, ("运营部-全部资源统计", "all_resource_count"))
        allocated_to_be_process_count = self.get_ele_text(mloc.allocated_to_be_process_count,
                                                          ("运营部-新分配待处理统计", "allocated_to_be_process_count"))
        my_following_count = self.get_ele_text(mloc.my_following_count, ("运营部-待跟进统计", "my_following_count"))
        appointment_count = self.get_ele_text(mloc.appointment_count, ("运营部-预约访统计", "appointment_count"))
        return all_resource_count, allocated_to_be_process_count, my_following_count, appointment_count

    # 我的资源-学科部/市场部统计
    def get_my_depart_count(self):
        all_resource_count = self.get_ele_text(mloc.all_resource_count, ("学科部/市场部-全部资源统计", "all_resource_count"))
        allocated_to_be_process_count = self.get_ele_text(mloc.allocated_to_be_process_count,
                                                          ("学科部/市场部-新分配待处理统计", "allocated_to_be_process_count"))
        my_following_count = self.get_ele_text(mloc.my_following_count, ("学科部/市场部-待跟进统计", "my_following_count"))
        branch_following_count = self.get_ele_text(mloc.branch_following_count,
                                                   ("学科部/市场部-校区待跟进统计", 'branch_following_count'))
        appointment_count = self.get_ele_text(mloc.appointment_count, ("学科部/市场部-预约访统计", "appointment_count"))
        return all_resource_count, allocated_to_be_process_count, my_following_count, branch_following_count, appointment_count



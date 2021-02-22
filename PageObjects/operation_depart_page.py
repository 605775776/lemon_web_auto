# coding:utf-8
# 2021/2/5 10:52
# Author:dsw

from PageLocators.operation_depart_page_locs import OperationDepartPageLocs as loc
from PageLocators.index_page_locs import IndexPageLocs as iloc
from PageLocators.operation_depart_page_locs import OperationDepartPageLocs as oloc
from Common.basepage import BasePage


class OperationPage(BasePage):

    def add_resource(self):
        a = self.get_element(oloc.first_resource_contact_name, ("", ''))
        print(a.text)
        self.click_element(loc.add_resource, ("首页-添加资源", "add_resource"))

    # 我的资源-运营部
    def get_resource_count(self):
        all_resource_count = self.get_ele_text(loc.all_resource_count, ("首页-点击我的资源", "all_resource_count"))
        allocated_to_be_process_count = self.get_ele_text(loc.allocated_to_be_process_count, ("首页-点击我的资源", "allocated_to_be_process_count"))
        my_following_count = self.get_ele_text(loc.my_following_count, ("首页-点击我的资源", "my_following_count"))
        appointment_count = self.get_ele_text(loc.appointment_count, ("首页-点击我的资源", "appointment_count"))
        return (all_resource_count, allocated_to_be_process_count, my_following_count, appointment_count)
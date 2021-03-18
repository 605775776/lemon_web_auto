# coding:utf-8
# 2021/3/17 9:43
# Author:dsw
import time

from Common.basepage import BasePage
from PageLocators.depart_page_locs import DepartPageLocs as dloc
from PageLocators.allocate_page_locs import AllocatePageLocs as alloc


class DepartResourcePage(BasePage):

    def get_depart_count(self):
        all_resource_count = int(self.get_ele_text(dloc.all_resource_count, ("部门资源-全部资源统计", 'all_resource_count')))
        allocated_to_be_process_count = int(self.get_ele_text(dloc.allocated_to_be_process_count, ("部门资源-已分配待处理", 'allocated_to_be_process_count')))
        unallocate_branch_count = int(self.get_ele_text(dloc.unallocated_branch_count, ("部门资源-未分配校区统计", 'unallocated_branch_count')))
        foot_all_resource_count = int((self.get_ele_text(dloc.foot_count, ("部门资源-共x条资源统计", 'foot_count')))[2: -2])
        return all_resource_count, allocated_to_be_process_count, unallocate_branch_count, foot_all_resource_count

    def switch_radio_to_all(self):
        print("全部")
        self.click_element(alloc.radio_1, ("通用-点击全部", 'radio_1'))
        time.sleep(1)

    def switch_radio_to_unallocate(self):
        self.click_element(alloc.radio_2, ("通用-点击未分配radio", 'radio_2'))
        time.sleep(1)

    def switch_radio_to_allocated(self):
        self.click_element(alloc.radio_3, ("通用-点击已分配", 'radio_3'))
        time.sleep(1)
        print("已分配")



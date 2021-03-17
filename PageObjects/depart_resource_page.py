# coding:utf-8
# 2021/3/17 9:43
# Author:dsw

from Common.basepage import BasePage
from PageLocators.depart_page_locs import DepartPageLocs as dloc


class DepartResourcePage(BasePage):

    def get_depart_count(self):
        all_resource_count = int(self.get_ele_text(dloc.all_resource_count, ("部门资源-全部资源统计", 'all_resource_count')))
        allocated_to_be_process_count = int(self.get_ele_text(dloc.allocated_to_be_process_count, ("部门资源-已分配待处理", 'allocated_to_be_process_count')))
        unallocate_branch_count = int(self.get_ele_text(dloc.unallocated_branch_count, ("部门资源-未分配校区统计", 'unallocated_branch_count')))
        foot_all_resource_count = int((self.get_ele_text(dloc.foot_count, ("部门资源-共x条资源统计", 'foot_count')))[2: -2])
        return all_resource_count, allocated_to_be_process_count, unallocate_branch_count, foot_all_resource_count


# coding:utf-8
# 2021/3/16 17:05
# Author:dsw

from Common.basepage import BasePage
from PageLocators.branch_resource_page_locs import BranchPageLocs as bloc

class BranchPage(BasePage):


    # 全部资源页面
    # 全部资源页面资源数量统计
    def get_branch_resource_count(self):
        all_resource_count = int(self.get_ele_text(bloc.all_resource_count, ("校区资源页面-全部资源数量统计", 'all_resource_count')))
        allocated_to_follow_count = int(self.get_ele_text(bloc.allocated_to_follow_count, ("校区资源页面-已分配待跟进数量统计", 'allocated_to_follow_count')))
        not_allocated_branch_belonger = int(self.get_ele_text(bloc.not_allocate_branch_belonger_count, ("校区资源页面-未分配校区归属人数量统计", 'not_allocate_branch_belonger_count')))
        foot_all_resource_count = int((self.get_ele_text(bloc.foot_count, ("部门资源-共x条资源统计", 'foot_count')))[2: -2])
        return all_resource_count, allocated_to_follow_count, not_allocated_branch_belonger, foot_all_resource_count


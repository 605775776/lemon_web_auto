# coding:utf-8
# 2021/2/24 14:14
# Author:dsw

from selenium.webdriver.common.by import By


class BranchPageLocs:

    # 全部资源页面

#全部资源统计

# 已分配待跟进页面

# 已分配待跟进统计

# 全部radio

# 未分配校区归属人radio

# 已分配校区归属人radio

# 添加资源按钮

# 批量添加分配校区归属人按钮

# 导出按钮

    # 资源列表-选中第一个资源checkbox
    checkbox_selected = (By.XPATH, "((//table[@class='el-table__body'])[3]//input)[1]")

    # 资源列表-第一个资源-资源详情
    first_resource_detail = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[1]")

    # 资源列表-第一个资源-分配校区归属人
    allocate_branch_belonger = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[2]")

    # 资源列表-第一个资源-修改
    modify_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")

    # 资源列表-第一个资源-删除
    delete_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")
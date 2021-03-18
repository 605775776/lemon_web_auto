# coding:utf-8
# 2021/1/19 14:50
# Author:dsw
# 部门资源页面元素定位
from selenium.webdriver.common.by import By


class DepartPageLocs:
    # --------------------------全部资源页面--------------------------
    # 全部资源页面
    all_resource_button = (By.XPATH, "//div[@id='tab-total']")

    # 已分配待处理页面
    new_Allocated_To_Branch = (By.XPATH, "//div[@id='tab-newAllocatedToBranch']")

    # 全部资源统计
    all_resource_count = (By.XPATH, "//div[@id='tab-total']/span/span")

    # 已分配待处理统计
    allocated_to_be_process_count = (By.XPATH, "//div[@id='tab-newAllocatedToBranch']//span[@class='font-bold']")

    # 资源未分配校区统计
    unallocated_branch_count = (By.XPATH, "//div[@class='message-tip']/span")

    # 添加资源按钮
    add_resource = (By.XPATH, "//span[text()='添加资源']")

    # 批量分配部门归属人
    batch_allocate_depart_belonger = (By.XPATH, "//span[text()='批量分配部门归属人']")

    # 批量分配校区
    batch_allocate_branch = (By.XPATH, "//span[text()='批量分配校区']")

    # 导入
    import_button = (By.XPATH, "//span[text()='导入']")

    # 导出
    export_button = (By.XPATH, "//span[text()='导出']")

    # 资源列表-第一个资源-资源详情
    first_resource_detail = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[1]")

    # 资源列表-第一个资源-分配部门归属人
    allocate_depart_belonger = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[2]")

    # 资源列表-第一个资源-分配校区
    allocate_branch = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")

    # 资源列表-第一个资源-修改
    modify_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")
    # depart_first_resource_modify = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[5]")

    # 资源列表-第一个资源-删除
    delete_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[5]")

    # 资源列表-选中第一个资源checkbox
    checkbox_selected = (By.XPATH, "(//table[@class='el-table__body'])[2]//label[1]")

    # 共x条
    foot_count = (By.XPATH, "//span[@class='el-pagination__total']")


# ---------------------已分配待处理页面------------------

    # 资源列表-第一个资源-资源详情
    first_resource_detail = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[1]")

    # 资源列表-第一个资源-分配部门归属人
    allocate_depart_belonger = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[2]")

    # 资源列表-第一个资源-修改
    not_allowed_modify_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")

    # 资源列表-第一个资源-删除
    not_allowed_delete_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")

    # toast消息文本
    msg = (By.XPATH, "(//p[@class='el-message__content'])[last()]")

    # tips提示消息文本
    tips = (By.XPATH, "//div[@class='el-form-item__error']")

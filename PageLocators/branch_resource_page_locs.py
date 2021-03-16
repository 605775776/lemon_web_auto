# coding:utf-8
# 2021/2/24 14:14
# Author:dsw

from selenium.webdriver.common.by import By


class BranchPageLocs:

# 全部资源页面
    # 全部资源统计
    all_resource_count = (By.XPATH, "//div[@id='tab-total']//span[@class='font-bold']")
# 已分配待跟进页面
    # 今日跟进按钮
    follow_today = (By.XPATH, "//button/span[text()='今日']")
    # 未来三天跟进按钮
    follow_in_three_days = (By.XPATH, "//button/span[text()='未来三天']")

    # 超时未跟进按钮
    unfollow = (By.XPATH, "//button/span[text()='超时未跟进']")


    # 有X条资源未分配校区归属人统计
    not_allocate_branch_belonger_count = (By.XPATH, "//div[@class='message-tip']/span")
    # 已分配待跟进统计
    allocated_to_follow_count = (By.XPATH, "//div[@id='tab-waitForFollowUp']//span[@class='font-bold']")
    # 全部radio
    radio_1 = (By.XPATH, "(//span[@class='el-radio__label'])[1]")
    # 未分配校区归属人radio
    radio_2 = (By.XPATH, "(//span[@class='el-radio__label'])[2]")
    # 已分配校区归属人radio
    radio_3 = (By.XPATH, "(//span[@class='el-radio__label'])[3]")

    # 添加资源按钮
    add_resource = (By.XPATH, "//button/span[text()='添加资源']")
    # 批量添加分配校区归属人按钮
    batch_add_resource = (By.XPATH, "//button/span[text()='批量分配校区资源']")
    # 导出按钮
    export_button = (By.XPATH, "//button/span[text()='导出']")

    # 资源列表
    # 第一个资源的课程详情
    resouce_detail = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[1]")

    # 第一个资源的分配校区归属人
    allocate_branch_belonger = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[2]")

    # 第一个资源的修改按钮
    modify_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")

    # 第一个资源的删除资源
    delete_resource = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")

    # 当前页面总数量统计
    all_page_count = (By.XPATH, "//span[@class='el-pagination__total']")

    #





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
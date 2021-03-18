# coding:utf-8
# 2021/1/19 14:52
# Author:dsw
from selenium.webdriver.common.by import By
class MyResourcePageLocs:


    # 全部资源
    tab_total = (By.XPATH, "//div[@id='tab-total']")


    # 我的资源-添加资源
    add_resource = (By.XPATH, "//span[text()='添加资源']")

    # 我的资源-导出
    export = (By.XPATH, "//span[text()='导出']")

    # 查询按钮
    search_button = (By.XPATH, "//button/span[text()='查询']")

    # 重置按钮
    reset_button = (By.XPATH, "//button/span[text()='重置']")

    # 全部资源统计
    all_resource_count = (By.XPATH, "//div[@id='tab-total']//span[@class='font-bold']")

    # 新分配待处理统计
    allocated_to_be_process_count = (By.XPATH, "//div[@id='tab-newAllocation']//span[@class='font-bold']")

    # 我的待跟进统计
    my_following_count = (By.XPATH, "//div[@id='tab-overtime']/span/span")

    # 校区待跟进统计
    branch_following_count = (By.XPATH, "//div[@id='tab-followUpPlanBeforeFuture3Days']/span/span")

    # 预约访（待办）统计
    appointment_count = (By.XPATH, "//div[@id='tab-appointment']/span/span")

    # 校长未分配校区归属人统计
    unallocate_branch_belonger = (By.XPATH, "//div[@class='message-tip']/span[@class='count']")

    # 共x条资源
    foot_count = (By.XPATH, "//span[@class='el-pagination__total']")


    # 资源列表-第一个资源-资源详情
    first_resource_detail = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[1]")

    # 资源列表-第一个资源-跟进
    first_resource_follow = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[2]")

    # 资源列表-第一个资源-签约
    my_first_resource_sign = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")
    depart_first_resource_sign = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")

    # 资源列表-第一个资源-试听
    my_first_resource_prelisten = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[4]")
    depart_first_resource_prelisten = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[5]")

    # 资源列表-第一个资源-修改
    my_first_resource_modify = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[5]")
    depart_first_resource_modify = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[6]")

    # 资源列表-第一个资源-预约访
    my_first_resource_appointment = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[6]")
    depart_first_resource_appointment = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[7]")

    # 资源列表-第一个资源-分配校区
    first_resource_allocate_branch = (By.XPATH, "((//table[@class='el-table__body'])[3]//i)[3]")

    # 关键词搜索
    key_search = (By.XPATH, "//label[text()='关键词搜索']/following-sibling::div//input")

    # 按联系电话
    search_by_phone = (By.XPATH, "//span[text()='按联系电话']")

    # 按联系电话输入框
    search_by_phone_input =(By.XPATH, "//input[@placeholder='请输入联系电话']")

    # 按联系人
    search_by_contactname = (By.XPATH, "//span[text()='按联系人']")

    # 按联系人输入框
    search_by_contactname_input = (By.XPATH, "//input[@placeholder='请输入联系人姓名']")

    # 按学生姓名
    search_by_studentname = (By.XPATH, "//span[text()='按学生姓名']")

    # 按学生姓名输入框
    search_by_studentname_input = (By.XPATH, "//input[@placeholder='请输入学生姓名']")

    # 按资源编号
    search_by_resourceNo = (By.XPATH, "//span[text()='按资源编号']")

    # 按资源编号输入框
    search_by_resourceNo_input = (By.XPATH, "//input[@placeholder='请输入资源编号']")

    # 按日期查询
    search_by_date = (By.XPATH, "(//div[@class='el-input el-input--small el-input--suffix'])[2]")

    # 按日期查询-资源日期
    resource_date = (By.XPATH, "//span[text()='资源日期']")

    # 按日期查询-最近一次跟进日期
    last_follow_date = (By.XPATH, "//span[text()='最近一次跟进日期']")

    # 按日期查询-最迟回访日期
    late_visit_date = (By.XPATH, "//span[text()='最迟回访日期']")

    # 开始时间-结束时间
    start_time = (By.XPATH, "//input[@placeholder='开始时间']")

    # 最近一周
    recent_week = (By.XPATH, "//button[text()='最近一周']")

    # 最近一个月
    recent_month = (By.XPATH, "//button[text()='最近一个月']")

    # 最近三个月
    recent_three_months = (By.XPATH, "//button[text()='最近三个月']")

    # 资源进展筛选
    resource_progress = (By.XPATH, "//input[@placeholder='请选择资源进展']")

    # 资源进展-待回电
    resource_progress_pre_phone = (By.XPATH, "//span[text()='待回电']")

    # 资源进展-已回电
    resource_progress_phoned = (By.XPATH, "//span[text()='已回电']")

    # 资源进展-已上门
    resource_progress_visit = (By.XPATH, "//span[text()='已上门']")

    # 资源进展-无法联系上
    resource_progress_uncall = (By.XPATH, "//span[text()='无法联系上']")

    # 资源进展-不再跟进/死单
    resource_progress_never = (By.XPATH, "//span[text()='不再跟进/死单']")

    # 资源进展-已成单
    resource_progress_order = (By.XPATH, "//span[text()='已成单']")

    first_resource_contact_name = (By.XPATH, "(((//tbody)[1]/tr)[1]/td)[1]/div")

    # 已分配资源的提示语
    allocated_msg = (By.XPATH, "//p[text()='资源已分配到校区，不允许再次分配']")


















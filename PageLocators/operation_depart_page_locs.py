# coding:utf-8
# 2021/1/19 14:52
# Author:dsw
from selenium.webdriver.common.by import By
class OperationDepartPageLocs:


    # 我的资源-运营部
    operation_depart = (By.XPATH, "//div[@id='tab-1']")

    # 我的资源-学科部
    subject_depart = (By.XPATH, "//div[@id='tab-2']")

    # 我的资源-市场部
    market_depart = (By.XPATH, "//div[@id='tab-3']")

    # 我的资源-添加资源
    add_resource = (By.XPATH, "//span[text()='添加资源']")

    # 我的资源-导出
    export = (By.XPATH, "//span[text()='导出']")

    # 查询按钮
    search_button = (By.XPATH, "//button/span[text()='查询']")

    # 重置按钮
    reset_button = (By.XPATH, "//button/span[text()='重置']")

    # 全部资源统计
    all_resource_count = (By.XPATH, "(//div[@class='count'])[1]")

    # 新分配待处理统计
    allocated_to_be_process_count = (By.XPATH, "(//div[@class='count'])[2]")

    # 我的待跟进统计
    my_following_count = (By.XPATH, "(//div[@class='count'])[3]")

    # 预约访（待办）统计
    appointment_count = (By.XPATH, "(//div[@class='count'])[4]")

    # 资源列表-第一个资源-资源详情
    first_resource_detail = (By.XPATH, "(//i[@class='hifont hi-xiangqing list-opera-icon el-popover__reference'])[1]")

    # 资源列表-第一个资源-跟进
    first_resource_follow = (By.XPATH, "(//i[@class='hifont hi-genjin list-opera-icon el-popover__reference'])[1]")

    # 资源列表-第一个资源-签约
    first_resource_sign = (By.XPATH, "(//i[@class='hifont hi-qianyue list-opera-icon el-popover__reference'])[1]")

    # 资源列表-第一个资源-试听
    first_resource_prelisten = (By.XPATH, "(//i[@class='hifont hi-shiting list-opera-icon el-popover__reference'])[1]")

    # 资源列表-第一个资源-修改
    first_resource_modify = (By.XPATH, "(//i[@class='hifont hi-xiugai list-opera-icon el-popover__reference'])[1]")

    # 资源列表-第一个资源-预约访
    first_resource_appointment = (By.XPATH, "(//i[@class='hifont hi-yuyuefang list-opera-icon el-popover__reference'])[1]")



    # 关键词搜索
    key_search = (By.XPATH, "//div[@class='el-input el-input--small el-input--suffix']")

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
    resource_progress_never = (By.XPATH, "//span[text()='已成单']")




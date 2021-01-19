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


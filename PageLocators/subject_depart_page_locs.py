# coding:utf-8
# 2021/1/19 14:50
# Author:dsw

from selenium.webdriver.common.by import By
class OperationDepartPageLocs:


    # 学科部-全部资源
    all_resource_count = (By.XPATH, "(//div[@class='count'])[1]")

    # 学科部-新分配待处理
    all_resource_count = (By.XPATH, "(//div[@class='count'])[2]")

    # 学科部-我的待跟进
    all_resource_count = (By.XPATH, "(//div[@class='count'])[3]")

    # 学科部-校区待跟进
    all_resource_count = (By.XPATH, "(//div[@class='count'])[4]")

    # 学科部-预约访待办
    all_resource_count = (By.XPATH, "(//div[@class='count'])[5]")

    #  校长分配校区归属人-全部按钮
    all_resource_radio = (By.XPATH, "(//span[@class='el-radio__inner'])[1]")

    #  校长分配校区归属人-未分配按钮
    all_resource_radio = (By.XPATH, "(//span[@class='el-radio__inner'])[2]")

    #  校长分配校区归属人-已分配按钮
    all_resource_radio = (By.XPATH, "(//span[@class='el-radio__inner'])[3]")
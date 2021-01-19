# coding:utf-8
# 2021/1/19 16:05
# Author:dsw

from selenium.webdriver.common.by import By

class AddAppointmentPageLocs:

    # 约访校区
    appointment_school = (By.XPATH, "(//form[@class='el-form el-form--inline'])[2]//input[@placeholder='请选择校区']")

    # 约访对象
    appointment_object = (By.XPATH, "//input[@placeholder='请填写约访对象']")

    # 约访日期
    appointment_date = (By.XPATH, "//input[@placeholder='请选择预约日期']")

    # 约访日期为今天
    appointment_date_selected= (By.XPATH, "//td[@class='available today']//span")

    # 预约时间
    appointment_time = (By.XPATH, "//input[@placeholder='请选择预约时间']")

    # 咨询难点-暂无
    none_difficulty = (By.XPATH, "(//span[text()='暂无'])[1]")

    # 咨询难点-其他
    other_difficulty = (By.XPATH, "(//div[@class='el-row el-row--flex']//span[text()='其他'])[1]")

    # 咨询难点-自定义
    custom_difficulty = (By.XPATH, "//input[@placeholder='请自定义咨询难点']")

    # 需求支持-暂无
    none_support = (By.XPATH, "(//span[text()='暂无'])[2]")

    # 需求支持-其他
    other_support = (By.XPATH, "(//div[@class='el-row el-row--flex']//span[text()='其他'])[2]")

    # 需求支持-自定义
    custom_support = (By.XPATH, "//input[@placeholder='请自定义需求支持']")

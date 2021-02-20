# coding:utf-8
# 2021/1/19 16:05
# Author:dsw

from selenium.webdriver.common.by import By

class AddAppointmentPageLocs:

    # 约访校区
    appointment_school = (By.XPATH, "(//form[@class='el-form el-form--inline'])[2]//input[@placeholder='请选择校区']")

    # 默认选中海沧未来海岸培英精品班校区
    appointment_school_selected = (By.XPATH, "(//body/div)[last()]//li/span")

    # 约访对象
    appointment_object = (By.XPATH, "//input[@placeholder='请填写约访对象']")

    # 默认约访对象为当前资源的联系人姓名
    appointment_object_first_contact_name = (By.XPATH, "((//tr[@class='el-table__row'])[1]//td)[1]/div")
    # appointment_object_first_contact_name = (By.CSS_SELECTOR, "tr.el-table__row>td>div")
    # 约访日期
    appointment_date = (By.XPATH, "//input[@placeholder='请选择预约日期']")

    # 约访日期为今天
    appointment_date_selected= (By.XPATH, "//td[@class='available today']//span")

    # 约访日期选中下个月
    # date_next_month = (By.CSS_SELECTOR, "div.el-date-picker__header>button:nth-child(4)>i")
    date_next_month = (By.XPATH, "//button[@aria-label='下个月']")

    # 约访日期选择下个月1号
    date_first_day = (By.XPATH, "//td[@class='prev-month']/following-sibling::td//span")

    # 预约时间
    appointment_time = (By.XPATH, "//input[@placeholder='请选择预约时间']")

    # 预约时间的确定按钮
    time_confirm = (By.XPATH, "//button[text()='确定']")

    # 咨询难点-暂无
    none_difficulty = (By.XPATH, "(//span[text()='暂无'])[1]")

    # 咨询难点-其他
    other_difficulty = (By.XPATH, "(//div[@class='el-row el-row--flex']//span[text()='其他'])[1]")

    # 难点列表
    difficulty_list_2 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[2]")
    difficulty_list_3 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[3]")
    difficulty_list_4 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[4]")
    difficulty_list_5 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[5]")
    difficulty_list_6 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[6]")
    difficulty_list_7 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[7]")
    difficulty_list_8 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[8]")
    difficulty_list_9 = (By.XPATH, "(//label[@for='consultingSpots']/following-sibling::div/div/label)[9]")

    # 咨询难点-自定义
    custom_difficulty = (By.XPATH, "//input[@placeholder='请自定义咨询难点']")

    # 需求支持-暂无
    none_support = (By.XPATH, "(//span[text()='暂无'])[2]")

    # 需求支持-其他
    other_support = (By.XPATH, "(//div[@class='el-row el-row--flex']//span[text()='其他'])[2]")

    # 需求支持-自定义
    custom_support = (By.XPATH, "//input[@placeholder='请自定义需求支持']")

    # 补充说明
    remark = (By.XPATH, "//textarea")

    # 确定按钮
    confirm = (By.XPATH, "//span[text()='确 定']")

    # 取消按钮
    cancel = (By.XPATH, "//span[text()='取 消']")

    # 预约访右上角关闭窗口
    close_iframe = (By.XPATH, "//span[text()='预约访']/..//i")

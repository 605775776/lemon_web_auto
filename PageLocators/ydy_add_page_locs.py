# coding:utf-8
# 2021/3/3 9:56
# Author:dsw


from selenium.webdriver.common.by import By

class YdyAddPageLocs:

    # 课程名称
    course_title = (By.XPATH, "//input[@placeholder='请填写课程名称']")

    # 年级
    course_grade = (By.XPATH, "//input[@placeholder='请选择年级']")

    # 年级-第一个
    course_grade_senior = (By.XPATH, "//body/div[last()]//li")

    # 课程类型
    course_kind = (By.XPATH, "//input[@placeholder='请选择课程类型']")


    # ----------------------个性化----------------------
    # 课程类型 面授1对1
    face2face = (By.XPATH, "//body/div[last()]//li/span[text()='面授1对1']")

    # 课程类型 在线1对1
    online = (By.XPATH, "//body/div[last()]//li/span[text()='在线1对1']")

    # 课程类型 MVP课程
    MVP = (By.XPATH, "//body/div[last()]//li/span[text()='MVP课程']")

    # 课程类型 全日制课程
    full_time = (By.XPATH, "//body/div[last()]//li/span[text()='全日制课程']")

    # ---------------------------------佳音 -----------------------------
    course_sub_kind = (By.XPATH, "//input[@placeholder='请选择课程子类型']")

    # 线上外教
    online_foreigner = (By.XPATH, "(//body/div[last()]//li)[1]")

    # VIP课程
    VIP = (By.XPATH, "(//body/div[last()]//li)[2]")




    # 课程校区
    # 应用全部校区
    applied_by_all_branch = (By.XPATH, "//span[text()='应用全部校区']")
    # 选择校区 列表返回第一个
    branch_list_01 = (By.XPATH, "(//body/div[last()]//li)[1]")
    branch_list_02 = (By.XPATH, "(//body/div[last()]//li)[2]")
    branch_list_03 = (By.XPATH, "(//body/div[last()]//li)[3]")
    branch_list_04 = (By.XPATH, "(//body/div[last()]//li)[4]")
    branch_list_05 = (By.XPATH, "(//body/div[last()]//li)[5]")
    branch_list_06 = (By.XPATH, "(//body/div[last()]//li)[6]")
    branch_list_07 = (By.XPATH, "(//body/div[last()]//li)[7]")
    # 开课日期输入框
    input_start_date = (By.XPATH, "//input[@placeholder='请选择开课日期']")

    # 开课日期 当天
    start_date = (By.XPATH, "//td[@class='available today']")
    # 结课日期 暂不修改
    # 课程长度 暂不修改
    # 课时单价
    unit_price = (By.XPATH, "//input[@placeholder='请输入价格']")
    # 售卖方式
    sale_method = (By.XPATH, "//input[@placeholder='请选择售卖方式']")

    # 仅ERP售卖
    sale_method_1 = (By.XPATH, "//body/div[last()]//li/span[text()='仅ERP售卖']")

    # 仅家长端售卖
    sale_method_2 = (By.XPATH, "//body/div[last()]//li/span[text()='仅家长端售卖']")

    # 通用
    sale_method_3 = (By.XPATH, "//body/div[last()]//li/span[text()='通用']")

    # 销售类型
    sale_type = (By.XPATH, "//input[@placeholder='请选择销售类型']")

    # 正价销售
    sale_type_1 = (By.XPATH, "//body/div[last()]//li/span[text()='正价销售']")
    # 引流活动
    sale_type_2 = (By.XPATH, "//body/div[last()]//li/span[text()='引流活动']")

    # 免费赠送
    sale_type_3 = (By.XPATH, "//body/div[last()]//li/span[text()='免费赠送']")

    # 课时折后单价
    discount_unit_price = (By.XPATH, "(//input[@placeholder='请输入价格'])[2]")
    # 上架时间
    sale_time = (By.XPATH, "//input[@placeholder='请选择上架时间']")

    # 上架时间选择今天
    sale_time_today = (By.XPATH ,"//table[@class='el-date-table']//td[@class='available today']")
    # 确定添加
    confirm_button = (By.XPATH, "//button/span[text()='确定添加']")


    # 取消
    cancel_button = (By.XPATH, "//button/span[text()='取消']")

    # 课程编码
    course_encoding = (By.XPATH, "//span[text()='课程编码：']/following-sibling::span[@class='adddone-con']")

    # 课程名称
    course_title_add_done = (By.XPATH, "//span[text()='课程名称：']/following-sibling::span[@class='adddone-con']")

    # 继续添加
    continue_to_add_button = (By.XPATH, "//button/span[text()='继续添加']")

    # 返回按钮
    return_button = (By.XPATH, "//button/span[text()='返回']")

    # 添加时间
    create_time = (By.XPATH, "//span[text()='添加时间：']/following-sibling::span[@class='adddone-con']")



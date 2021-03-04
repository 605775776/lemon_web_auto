# coding:utf-8
# 2021/3/3 9:53
# Author:dsw

from selenium.webdriver.common.by import By

class YdyPageLocs:


    # ------------------------------查询部分---------------------------------------

    # 切换关键词搜索
    switch_keywords = (By.XPATH, "(//div[@class='search-container']//input)[1]")

    # 找到按课程编码
    search_by_encode = (By.XPATH, "//li/span[text()='按课程编码']")

    # 按课程名称搜索
    input_search_by_title = (By.XPATH, "//input[@placeholder='请输入课程名称']")

    # 按课程编码搜索
    input_search_by_encode = (By.XPATH, "//input[@placeholder='请输入课程编码']")

    # 是否全部校区
    select_all_branch = (By.XPATH, "//label[text()='是否全部校区']/following-sibling::div//input")

    # 是
    option_yes = (By.XPATH, "//li/span[text()='是']")

    # 否
    option_no = (By.XPATH, "//li/span[text()='否']")

    # 选择校区
    select_branch = (By.XPATH, "//input[@placeholder='请选择校区']")

    # 校区下拉列表返回第一个
    li_branch_1 = (By.XPATH, "(//body/div[last()]//ul/li)[1]")

    # 选择年级
    select_grade = (By.XPATH, "//input[@placeholder='请选择年级']")

    # 默认选择高一
    option_senior = (By.XPATH, "//body/div[last()]//li/span[text()='高一']")

    # 清空课程状态
    clear_course_status = (By.XPATH, "//label[text()='课程状态']/following-sibling::div//i[@class='el-select__caret el-input__icon el-icon-arrow-up']")

    # 课程状态选择
    select_course_status = (By.XPATH, "//input[@placeholder='请选择课程状态']")

    # 已作废
    li_status_1 = (By.XPATH, "(//body/div[last()]//li)[1]")

    # 正常
    li_status_2 = (By.XPATH, "(//body/div[last()]//li)[2]")

    # 已结课
    li_status_3 = (By.XPATH, "(//body/div[last()]//li)[3]")

    # 课程类型选择
    select_course_type = (By.XPATH, "//input[@placeholder='请选择课程类型']")

    # 面授1对1 （共用）
    face2face = (By.XPATH, "(//body/div[last()]//li)[1]")

    # -----------------------------个性化-----------------------------------------

    # 在线1对1
    online = (By.XPATH, "(//body/div[last()]//li)[2]")

    # MVP课程
    MVP = (By.XPATH, "(//body/div[last()]//li)[3]")

    # 全日制课程
    fulltime = (By.XPATH, "(//body/div[last()]//li)[4]")

    # --------------------------佳音-----------------------------------------------

    # 课程子类型选择
    select_course_kind_type = (By.XPATH, ("//input[@placehodler='请选择课程子类型']"))

    # 线上外教
    online_foreigner = (By.XPATH, "(//body/div[last()]//li)[1]")

    # VIP课程
    VIP = (By.XPATH, "(//body/div[last()]//li)[2]")

    # 上下架
    status = (By.XPATH, "//input[@placeholder='请选择上下架']")

    # 上架
    on = (By.XPATH, "//body/div[last()]//span[text()='上架']")

    # 下架
    off = (By.XPATH, "//body/div[last()]//span[text()='下架']")

    # 查询按钮
    search_button = (By.XPATH, "//button/span[text()='查询']")

    # 重置按钮
    reset_button = (By.XPATH, "//button/span[text()='重置']")

    # 添加课程
    add_course = (By.XPATH, "//button/span[text()='添加课程']")

    # 导入
    import_button = (By.XPATH, "//button/span[text()='导入']")

    # 导出
    export_button = (By.XPATH, "//button/span[text()='导出']")

    # 批量上架按钮
    batch_on = (By.XPATH, "//button/span[text()='批量上架']")

    # 批量下架按钮
    batch_off = (By.XPATH, "//button/span[text()='批量下架']")

    # 批量废弃按钮
    batch_abandon = (By.XPATH, "//button/span[text()='批量废弃']")

    # 课程数量统计
    count_str = (By.XPATH, "//span[@class='el-pagination__total']")


# coding:utf-8
# 2021/2/23 10:51
# Author:dsw
# 部门资源分配页面元素定位


from selenium.webdriver.common.by import By


class AllocatePageLocs:
    # -------------------------------部门资源页面的分配---------------------------
    # 输入归属校区
    input_branch = (By.XPATH, "//input[@placeholder='请输入校区搜索']")

    # 输入部门归属人姓名
    input_depart_belonger = (By.XPATH, "//input[@placeholder='请输入部门归属人姓名搜索']")

    # 确定按钮
    confirm_button = (By.XPATH, "//button/span[text()='确定']")

    # 取消按钮
    cancel_button = (By.XPATH, "//button/span[text()='取消']")

    # 选择下拉列表校区
    selected_branch = (By.XPATH, "//body/div[last()]//li")

    # 选择下拉列表中的用户 我的账户问题
    selected_depart_belonger = (By.XPATH, "//body/div[last()]//li[last()]")

    # 待分配资源数量 +'条'
    wait_allocate_resource_count_str = (By.XPATH, "//label[text()='待分配资源']/following-sibling::div/div/strong")

    # 已分配资源数量 +'条'
    allocated_resource_count_str = (By.XPATH, "//label[text()='待分配资源']/following-sibling::div/div/div/strong")

    # 已选择资源数量统计  "已选" + num +"条"
    selected_resource_count = (By.XPATH, "//label[text()='待分配资源']/following-sibling::div/div/div")
    #---------------------------------校区资源分配校区归属人---------------------------------------

    # 输入校区归属人
    input_branch_belonger = (By.XPATH, "//input[@placeholder='请输入校区归属人搜索']")

    # 选择校区归属人
    selected_branch_belonger = (By.XPATH, "//body/div[last()]//li")

    # 更新最迟回访日期
    update_button = (By.XPATH, "//span[text()='更新日期']")

    # 日期输入框
    input_date = (By.XPATH, "//input[@placeholder='选择日期']")

    # 更新日期默认选择下一天
    update_date = (By.XPATH, "//td[@class='available today current']/following-sibling::td")

    # 右上角关闭弹窗
    close_iframe = (By.XPATH, "//button[@aria-label='Close']")

    # 全部radio
    radio_1 = (By.XPATH, "(//span[@class='el-radio__label'])[1]")
    # 未分配校区归属人radio
    radio_2 = (By.XPATH, "(//span[@class='el-radio__label'])[2]")
    # 已分配校区归属人radio
    radio_3 = (By.XPATH, "(//span[@class='el-radio__label'])[3]")


# coding:utf-8
# 2021/2/23 10:51
# Author:dsw

from selenium.webdriver.common.by import By

class AllocatePageLocs:

    # 输入归属校区
    input_branch = (By.XPATH, "//input[@placeholder='请输入校区搜索']")

    # 输入部门归属人姓名
    input_depart_belonger = (By.XPATH, "//input[@placeholder='请输入部门归属人姓名搜索'")

    # 确定按钮
    confirm_button = (By.XPATH, "//button/span[text()='确定']")

    # 取消按钮
    cancel_button = (By.XPATH, "//button/span[text()='取消']")

    # 下拉列表校区
    selected_branch = (By.XPATH, "//body/div[last()]//span")

    # 待分配资源数量 +'条'
    wait_allocate_resource_count = (By.XPATH, "//label[text()='待分配资源']/following-sibling::div/div/strong")

    # 已分配资源数量 +'条'
    allocated_resource_count = (By.XPATH, "//label[text()='待分配资源']/following-sibling::div/div/div/strong")

    #
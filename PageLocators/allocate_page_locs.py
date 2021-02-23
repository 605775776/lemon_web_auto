# coding:utf-8
# 2021/2/23 10:51
# Author:dsw

from selenium.webdriver.common.by import By

class AllocatePageLocs:

    # 输入归属校区
    input_branch = (By.XPATH, "//input[@placeholder='请输入校区搜索']")

    # 确定按钮
    confirm_button = (By.XPATH, "//button/span[text()='确定']")

    # 取消按钮
    cancel_button = (By.XPATH, "//button/span[text()='取消']")

    # 下拉列表校区
    selected_branch = (By.XPATH, "//body/div[last()]//span")


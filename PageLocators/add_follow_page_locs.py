# coding:utf-8
# 2021/1/19 17:04
# Author:dsw
# 跟进资源页面元素定位

from selenium.webdriver.common.by import By

class add_follow_page_locs:

    # 本次跟进时间
    # 跟进方式
    # 资源进展
    resource_progress = (By.XPATH, "//input[@placeholder='请选择资源进展']")
    # 资源日期
    # 资源日期
    # 首次上门日期
    # 资源质量
    # 沟通内容
    # 最迟回访日期
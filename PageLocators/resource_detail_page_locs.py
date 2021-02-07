# coding:utf-8
# 2021/2/5 16:00
# Author:dsw

from selenium.webdriver.common.by import By

class ResourceDetailPageLocs:

    # 基本信息
    base_info = (By.XPATH, "//div[@id='tab-BaseInfo']")

    # 跟进记录
    follow_info = (By.XPATH, "//div[@id='tab-Follow']")

    # 约访记录
    appoint_info = (By.XPATH, "//div[@id='tab-Interview']")

    # 联系人
    contact_info = (By.XPATH, "//div[@id='tab-Contacts'")

    # 试听记录
    listen_info = (By.XPATH, "//div[@id='tab-Audition'")

    # 成单记录
    order_info = (By.XPATH, "//div[@id='tab-Order'")

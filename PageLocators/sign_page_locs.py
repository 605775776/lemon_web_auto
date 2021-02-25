# coding:utf-8
# 2021/2/25 14:07
# Author:dsw

from selenium.webdriver.common.by import By

class SignPageLocs:


    # 去报班
    goto_sign = (By.XPATH, "//button/span[text()='去报班']")
    # 已报班，请点这里回填订单号
    order_fill = (By.XPATH, "//div[@class='order-fill']")
    # 右上角关闭按钮
    close_button = (By.XPATH, "//div[@aria-label='签约']//i")

    # 创建新学员
    add_student = (By.XPATH, "//button/span[text()='创建新学员']")

    #--------------------erp系统--------------------

    # 保存学员
    create_student = (By.XPATH, "//button[text()='保存学员']")

    # 立即报班
    sign_now = (By.XPATH, "//button[text()='立即报班']")

    # 下一步
    next_step_button = (By.XPATH, "//button[@ng-click='nextStep(1,2)']")


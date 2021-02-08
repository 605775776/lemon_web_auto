# coding:utf-8
# 2021/2/5 16:25
# Author:dsw

from selenium.webdriver.common.by import By


class FollowPageLocs:
    # 跟进方式
    follow_method = (By.XPATH, "//div[@aria-label='跟进资源']//input[@placeholder='请选择']")

    # 微信或QQ
    follow_method_weixin = (By.XPATH, "//span[text()='微信或QQ']")

    # 电话
    follow_method_phone = (By.XPATH, "//span[text()='电话']")

    # 现场咨询
    follow_method_live = (By.XPATH, "//span[text()='现场咨询']")

    # 短信
    follow_method_message = (By.XPATH, "//span[text()='短信']")

    # 不再跟进
    follow_method_never_follow = (By.XPATH, "//span[text()='不再跟进']")

    # 家访
    follow_method_go_home = (By.XPATH, "//span[text()='家访']")

    # 资源进展
    resource_progress = (By.XPATH, "//div[@aria-label='跟进资源']//input[@placeholder='请选择资源进展']")

    # 已回电
    progress_phoned = (By.XPATH, "(//li[@class='el-select-dropdown__item']/span[text()='已回电'])[2]")

    # 已上门
    progress_homed = (By.XPATH, "(//li[@class='el-select-dropdown__item']/span[text()='已上门'])[2]")

    # 无法联系上
    progress_uncontact = (By.XPATH, "(//li[@class='el-select-dropdown__item']/span[text()='无法联系上'])[2]")

    # 不再跟进/死单
    progress_never_follow = (By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='不再跟进/死单']")

    # 首次上门日期为空时
    first_visit_date = (By.XPATH, "//label[@for='firstVisitDate']/parent::div//input")

    # 默认选择当天
    first_visit_date_today = (By.XPATH, "//td[@class='available today']//span")

    # 资源质量 5颗星
    resource_stars = (By.XPATH, "//label[@for='quality']/following::div/div/span[5]")

    # 沟通内容
    communicate_context = (By.XPATH, "//textarea[@placeholder='请填写沟通内容,800字以内']")

    # 最迟回访日期
    next_follow_update = (By.XPATH, "//label[@for='nextFollowUpDate']/following::input")

    # 最迟回访日期选择下一个月
    # next_month = (By.XPATH, "(//div[@class='el-date-picker__header']//button[@aria-label='下个月'])[2]")
    next_month = (By.CSS_SELECTOR, "div.el-date-picker__header>button>aria-label")

    # 下个月的1号
    next_month_1 = (By.XPATH, "//td[@class='available']/div/span")

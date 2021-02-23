#coding=gbk
from selenium.webdriver.common.by import By


class IndexPageLocs:

    # 招生入口元素
    entrance = (By.XPATH, "//span[text()='招生入口']")

    # 我的资源元素
    my_resource = (By.XPATH, "//span[text()='我的资源']")

    # 我的资源-运营部
    operation_depart = (By.XPATH, "//li/span[text()='运营部']")

    # 我的资源-学科部
    my_subject_depart = (By.XPATH, "//a[@href='/crm/my-resource/dis-dep']//span[text()='学科部']")

    # 我的资源-市场部
    my_market_depart = (By.XPATH, "//a[@href='/crm/my-resource/marketdep']//span[text()='市场部']")

    # 部门资源
    depart_resource = (By.XPATH, "//span[text()='部门资源']")

    # 部门资源-学科部
    depart_subject = (By.XPATH, "//a[@href='/crm/dept-resource/dis-dep']//span[text()='学科部']")
    # 部门资源-市场部
    depart_market = (By.XPATH, "//a[@href='/crm/dept-resource/marketdep']//span[text()='市场部']")

    # 校区资源
    branch_resource = (By.XPATH, "//a[@href='/crm/schoolresource']/li")

    # 资源转移
    resource_transfer = (By.XPATH, "//span[text()='资源转移']")

    # 资源解绑
    resource_unbind = (By.XPATH, "//span[text()='资源解绑']")

    # 约访管理
    appointment_manage = (By.XPATH, "//span[text()='约访管理']")

    # 校区
    branch = (By.XPATH, "//span[@class='title']/following-sibling::span")















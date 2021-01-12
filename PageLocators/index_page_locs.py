from selenium.webdriver.common.by import By


class IndexPageLocs:
    # # 用户名元素 -是否存在状态
    # exit_link = (By.XPATH, "//a[text()='退出']")

    # 招生入口元素
    entrance = (By.XPATH, "//span[text()='招生入口']")

    # 我的资源
    my_resource = (By.XPATH, "//span[text()='我的资源']")

    # 部门资源
    department_resource = (By.XPATH, "//span[text()='部门资源']")

    # 校区资源
    branch_resource = (By.XPATH, "//span[text()='校区资源']")

    # 资源转移
    resource_transfer = (By.XPATH, "//span[text()='资源转移']")

    # 资源解绑
    resource_unbind = (By.XPATH, "//span[text()='资源解绑']")

    # 约访管理
    appointment_manage = (By.XPATH, "//span[text()='约访管理']")

    # 我的资源-运营部
    operation_depart = (By.XPATH, "//div[@id='tab-1']")

    # 我的资源-学科部
    subject_depart = (By.XPATH, "//div[@id='tab-2']")

    # 我的资源-市场部
    market_depart = (By.XPATH, "//div[@id='tab-3']")
    #






    # # 关于我们
    # about_us = (By.XPATH, '//a[text()="关于我们"]')
    # # 用户昵称
    # user_link = (By.XPATH, '//a[@href="/Member/index.html"]')
    #
    # # 投标按钮 默认第一个
    # bid_button = (By.XPATH, "//a[@class='btn btn-special']")
    # # 第二个 找到分支 或者用find_elements找到全部再用下标
    # bid_button_2 = (By.XPATH, '//div[@class="b-unit"][2]//a[text()="抢投标"]')
    # # 第三个
    # bid_button_3 = (By.XPATH, '//div[@class="b-unit"][3]//a[text()="抢投标"]')
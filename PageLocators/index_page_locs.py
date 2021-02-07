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

    # 添加资源
    add_resource = (By.XPATH, "//button//span[text()='添加资源']")














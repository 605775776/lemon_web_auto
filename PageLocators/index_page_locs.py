from selenium.webdriver.common.by import By


class IndexPageLocs:
    # 用户名元素 -是否存在状态
    exit_link = (By.XPATH, "//a[text()='退出']")

    # 关于我们
    about_us = (By.XPATH, '//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')

    # 投标按钮 默认第一个
    bid_button = (By.XPATH, "//a[@class='btn btn-special']")
    # 第二个 找到分支 或者用find_elements找到全部再用下标
    bid_button_2 = (By.XPATH, '//div[@class="b-unit"][2]//a[text()="抢投标"]')
    # 第三个
    bid_button_3 = (By.XPATH, '//div[@class="b-unit"][3]//a[text()="抢投标"]')
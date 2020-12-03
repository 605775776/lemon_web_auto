from selenium.webdriver.common.by import By


class IndexPageLocs:
    # 用户名元素 -是否存在状态
    exit_link = (By.XPATH, "//a[text()='退出']")
    bid_button = (By.XPATH, "//a[@class='btn btn-special']")
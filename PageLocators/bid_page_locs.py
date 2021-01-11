from selenium.webdriver.common.by import By


class BidPageLocs:


    # 金额输入框
    money_input = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")

    # 标的余额元素
    # bid_money_text = (By.XPATH, "//div[contains(@class, 'money_overplus')]//span[text()='剩余： ']")
    # // span[text() =‘剩余：’] / following-silbing
    bid_money_text = (By.XPATH, '//div[@class="left fs-16 money_overplus"]//span[@class="mo_span4"]')

    # 投标按钮
    invest_button = (By.XPATH, "//button[@class='btn btn-special height_style']")

    # 投资成功弹出框 - 查看并激活按钮
    active_button_on_successPop = (By.XPATH, '//div[@class="layui-layer-content"]//button')

    # 投资失败 - 弹出框-提示信息
    invest_failed = (By.XPATH, '//div[@class="text-center"]')

    # 投资失败-弹出框-关闭弹出框
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class, "layui-layer-dialog")]//a')

from selenium.webdriver.common.by import By


class BidPageLocs:


    # ��������
    money_input = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")

    # ������Ԫ��
    # bid_money_text = (By.XPATH, "//div[contains(@class, 'money_overplus')]//span[text()='ʣ�ࣺ ']")
    # // span[text() =��ʣ�ࣺ��] / following-silbing
    bid_money_text = (By.XPATH, '//div[@class="left fs-16 money_overplus"]//span[@class="mo_span4"]')

    # Ͷ�갴ť
    invest_button = (By.XPATH, "//button[@class='btn btn-special height_style']")

    # Ͷ�ʳɹ������� - �鿴�����ť
    active_button_on_successPop = (By.XPATH, '//div[@class="layui-layer-content"]//button')

    # Ͷ��ʧ�� - ������-��ʾ��Ϣ
    invest_failed = (By.XPATH, '//div[@class="text-center"]')

    # Ͷ��ʧ��-������-�رյ�����
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class, "layui-layer-dialog")]//a')

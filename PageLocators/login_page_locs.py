from selenium.webdriver.common.by import By


class LoginPageLocs:

    # �û���
    user_input = (By.XPATH, "//input[@id='username']")

    # ����
    pwd_input = (By.XPATH, "//input[@id='password']")

    # ��֤��
    validateCode_input = (By.XPATH, "//input[@id='validateCode']")

    # ��¼��ť
    login_button = (By.XPATH, "//div[@class='btn btn-submit btn-block']")

    # ��ʾ��Ϣ
    # error_msg = (By.XPATH, "//div[@class='form-error-info']")
    entrance = (By.XPATH, "//span[text()='�������']")
#
# if __name__ == '__main__':
#     print(LoginPageLocs.entrance)
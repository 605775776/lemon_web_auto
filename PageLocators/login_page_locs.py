from selenium.webdriver.common.by import By


class LoginPageLocs:

    # 用户名
    user_input = (By.XPATH, "//input[@id='username']")

    # 密码
    pwd_input = (By.XPATH, "//input[@id='password']")

    # 验证码
    validateCode_input = (By.XPATH, "//input[@id='validateCode']")

    # 登录按钮
    login_button = (By.XPATH, "//div[@class='btn btn-submit btn-block']")

    # 提示信息
    # error_msg = (By.XPATH, "//div[@class='form-error-info']")
    entrance = (By.XPATH, "//span[text()='招生入口']")
#
# if __name__ == '__main__':
#     print(LoginPageLocs.entrance)
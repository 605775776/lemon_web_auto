from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageLocs:

    # 用户名
    user_input = (By.XPATH, "//input[@name='phone']")

    # 密码
    pwd_input = (By.XPATH, "//input[@name='password']")

    # 登录按钮
    login_button = (By.TAG_NAME, "button")

    # 提示信息
    error_msg = (By.XPATH, "//div[@class='form-error-info']")

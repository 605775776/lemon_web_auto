from PageLocators.login_page_locs import LoginPageLocs as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password, validateCode):
        self.input_text(loc.user_input, username, ("登录页面_输入用户名", 'user_input'))
        self.input_text(loc.pwd_input, password, ("登录页面_输入密码", 'pwd_input'))
        self.input_text(loc.validateCode_input, validateCode, ( "登录页面_输入密码", 'validateCode_input'))
        self.click_element(loc.login_button, ("登录页面_点击登录按钮", 'login_button'))

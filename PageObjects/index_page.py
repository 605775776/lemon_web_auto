from PageLocators.index_page_locs import IndexPageLocs as loc
from Common.basepage import BasePage


class IndexPage(BasePage):


    # 我的资源-添加资源
    def add_my_resource(self):
        self.click_element(loc.entrance, ("首页-点击招生入口", "entrance"))
        self.click_element(loc.my_resource, ("首页-点击我的资源", "my_resource"))
        self.click_element(loc.)

        self.input_text(loc.user_input, username, ("登录页面_输入用户名", 'user_input'))
        self.input_text(loc.pwd_input, password, ("登录页面_输入密码", 'pwd_input'))
        self.input_text(loc.validateCode_input, validateCode, ( "登录页面_输入密码", 'validateCode_input'))
        self.click_element(loc.login_button, ("登录页面_点击登录按钮", 'login_button'))
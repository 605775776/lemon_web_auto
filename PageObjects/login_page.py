
from PageLocators.login_page_locs import LoginPageLocs as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password, validateCode):
        self.input_text(loc.user_input, username, "登录页面_输入用户名")
        self.input_text(loc.pwd_input, password, "登录页面_输入密码")
        self.input_text(loc.validateCode_input, validateCode, "登录页面_输入密码")
        self.click_element(loc.login_button, "登录页面_点击登录按钮")

    def get_element_entrance(self):
        self.wait_ele_visible(loc.entrance, "登录首页-招生入口")
    # def msg_from_login_form(self):
    #     self.wait_ele_visible(loc.msg_from_login_form, "登录页面-等待登录表单的错误提示元素")
    #     eles = self.get_elements(loc.msg_from_login_form, "登录页面-获取登录表单的错误提示元素")
    #
    #     if len(eles) == 1:
    #         return eles[0].text
    #     elif len(eles) > 1:
    #         text_list =[]
    #         for el in eles:
    #             text_list.append(el.text)
    #         return text_list
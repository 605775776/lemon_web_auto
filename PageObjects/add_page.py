# coding:utf-8
# 2021/1/19 14:02
# Author:dsw

from PageLocators.add_page_locs import AddPageLocs as loc
from Common.basepage import BasePage


class AddPage(BasePage):


    def add_resource(self, student_name, ):
        self.input_text(loc.student_name, student_name, "添加资源页面_输入学生姓名", 'student_name')




    def login(self, username, password, validateCode):
        self.input_text(loc.user_input, username, ("登录页面_输入用户名", 'user_input'))
        self.input_text(loc.pwd_input, password, ("登录页面_输入密码", 'pwd_input'))
        self.input_text(loc.validateCode_input, validateCode, ( "登录页面_输入密码", 'validateCode_input'))
        self.click_element(loc.login_button, ("登录页面_点击登录按钮", 'login_button'))
# coding:utf-8
# 2021/1/19 14:02
# Author:dsw

from PageLocators.add_page_locs import AddPageLocs as loc
from Common.basepage import BasePage
from test_data.resource_data import ResourceGenerator as rg

class AddPage(BasePage):


    def add_resource(self, student_name, class_name, school_name, resource_desc, contact_phone, contact_remark, resource_birthday, recommend_teacher, resource_address):
        # self.click_element(loc.student_name, ("添加资源页面-输入学生姓名", 'student_name'))
        contact_name = student_name + '的父亲'

        self.input_text(loc.student_name, student_name, ("添加资源页面-输入学生姓名", 'student_name'))

        self.click_element(loc.resource_type, ("添加资源页面-输入资源类型", 'resource_type'))

        self.click_element(loc.resource_type_1, ("添加资源页面-选择校区前台电话", '校区前台电话'))
        self.click_element(loc.source_channel, ("添加资源页面-来源渠道", 'source_channel'))
        self.click_element(loc.source_channel_4, ("添加资源页面-来源渠道-宣传单", 'source_channel_4'))


        self.click_element(loc.resource_stars, ("添加资源页面-资源质量5颗星", 'resource_starts'))

        self.click_element(loc.resource_progress, ("添加资源页面-资源进展", 'resource_progress'))
        self.click_element(loc.resource_progress_pre_phone, ("添加资源页面-资源进展-待回电", 'resource_progress_pre_phone'))

        self.click_element(loc.first_visit_date, ("添加资源页面-首次上门日期", 'first_visit_date'))
        self.click_element(loc.first_visit_date_today, ("添加资源页面-首次上门日期选择今天", 'first_visit_date_today'))

        self.click_element(loc.late_visit_date, ("添加资源页面-最迟回访日期", "late_visit_date"))
        self.click_element(loc.late_visit_date_today, ("添加资源页面-最迟回访日期选择今天", "late_visit_date_today"))

        self.click_element(loc.collect_grade, ("添加资源页面-录入年级", "collect_grade"))
        self.click_element(loc.collect_grade_senior, ("添加资源页面-录入年级选择高一", "collect_grade_senior"))

        # self.click_element(loc.resource_class, ("添加资源页面-录入班级", 'resource_class'))
        self.input_text(loc.resource_class, class_name, ("添加资源页面-输入年级", 'class_name'))

        self.click_element(loc.school, ("添加资源页面-选择就读学校", 'school'))
        self.input_text(loc.school, school_name, ("添加资源页面-输入厦门市实验中学", 'school_name'))
        self.click_element(loc.school_name, ("添加资源页面-输入厦门市实验中学", 'school_name'))

        self.input_text(loc.resource_desc, resource_desc, ("添加资源页面-填写资源描述", 'resource_desc'))

        self.click_element(loc.contact_relationship, ("添加资源页面-选择联系人关系", 'contact_relationship'))
        self.click_element(loc.contact_relationship_father, ("添加资源页面-选择联系人关系-父亲", 'contact_relationship_father'))

        self.input_text(loc.contact_name, contact_name, ("添加资源页面-输入联系人姓名", 'contact_name'))
        self.input_text(loc.contact_phone, contact_phone, ("添加资源页面-输入联系人电话", 'contact_phone'))
        self.input_text(loc.contact_remark, contact_remark, ("添加资源页面-输入联系人电话", 'contact_remark'))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        self.click_element(loc.resource_sex_male, ("添加资源页面-性别男", 'resource-sex-male'))
        self.input_text(loc.resource_birthday, resource_birthday, ("添加资源页面-生日设置为2020-01-01", 'resource_birthday'))

        self.input_text(loc.recommend_teacher, recommend_teacher, ("添加资源页面-输入推荐老师", 'recommend_teacher'))
        self.click_element(loc.recommend_teacher_short, ("添加资源页面-推荐老师简称", 'recommend_teacher_short'))

        self.click_element(loc.intention_subject,("添加资源页面-意向科目", 'intention_subject'))
        self.click_element(loc.intention_subject_math, ("添加资源页面-意向科目-数学", 'intention_subject_math'))

        self.input_text(loc.resource_address, resource_address, ("添加资源页面-资源地址/小区",'resource_address'))

        self.click_element(loc.confirm_add, ("添加资源页面-确认添加", 'confirm_add'))

    def add_resource_data(self):
        student_name = rg().studentNameGenerator()
        class_name = rg().classNameGenerator()
        school_name = rg().schoolNameGenerator()
        resource_desc = rg().resourceDescGenerator()
        telephone = rg().phoneNORandomGenerator()
        contact_remark = rg().contactDescGenerator()
        birthday = rg().birthdayGenerator()
        teacher = rg().teacherGenerator()
        address = rg().addressGenerator()
        resource_data = (student_name, class_name, school_name, resource_desc, telephone, contact_remark, birthday, teacher, address)
        return resource_data
    # def login(self, username, password, validateCode):
    #     self.input_text(loc.user_input, username, ("登录页面_输入用户名", 'user_input'))
    #     self.input_text(loc.pwd_input, password, ("登录页面_输入密码", 'pwd_input'))
    #     self.input_text(loc.validateCode_input, validateCode, ( "登录页面_输入密码", 'validateCode_input'))
    #     self.click_element(loc.login_button, ("登录页面_点击登录按钮", 'login_button'))
    
    
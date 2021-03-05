# coding:utf-8
# 2021/3/4 14:53
# Author:dsw
import time

from Common.basepage import BasePage
from PageLocators.ydy_page_locs import YdyPageLocs as loc
from PageLocators.ydy_add_page_locs import YdyAddPageLocs as aloc

class YdyPage(BasePage):

    # 添加课程
    def add_course(self, course_name):
        time.sleep(2)
        count = self.get_ele_text(loc.count_str, ("课程数量", 'count_str'))
        print(count)
        count = int(count[2: -2])
        print(count)
        self.click_element(loc.add_course, ("添加课程", 'add_course'))
        self.input_text(aloc.course_title, course_name, ("输入课程名称", 'course_title'))
        self.click_element(aloc.course_grade, ("输入年级", 'course_grade'))
        self.click_element(aloc.course_grade_senior, ("输入高一", 'course_grade_senior'))
        self.click_element(aloc.course_kind, ("课程类型", 'course_kind'))
        self.click_element(aloc.face2face, ("课程类型-面授1对1", 'face2face'))

        time.sleep(0.5)
        self.click_element(aloc.course_sub_kind, ("课程子类型", 'course_sub_kind'))
        self.click_element(aloc.online_foreigner, ("课程子类型-线上外教", 'online_foreigner'))

        self.click_element(aloc.applied_by_all_branch, ("选择全部校区", 'applied_by_all_branch'))
        self.click_element(aloc.input_start_date, ("输入开课日期", 'input_start_date'))
        self.click_element(aloc.start_date, ("开课日期为今天", 'start_date'))
        self.input_text(aloc.unit_price, 100, ("输入课时单价：100", 'unit_price'))
        self.click_element(aloc.sale_method, ("售卖方式", 'sale_method'))
        self.click_element(aloc.sale_method_1, ("售卖方式选择仅erp售卖", 'sale_method_1'))
        self.click_element(aloc.sale_type, ("销售类型", 'sale_type'))
        self.click_element(aloc.sale_type_1, ("销售类型-正价销售", 'sale_type_1'))
        self.input_text(aloc.discount_unit_price, 80, ("输入课时折后单价：80", 'discount_unit_price'))
        self.click_element(aloc.sale_time, ("上架时间",  'sale_time'))
        self.click_element(aloc.sale_time_today, ("上架时间选择今天", 'sale_time_today'))
        # self.driver.execute_script('window.scrollBy(0,200)')

        # element = self.driver.find_element_by_xpath("//button/span[text()='确定添加']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # self.click_element(aloc.sale_time, ("上架时间", 'sale_time'))
        self.get_element(aloc.confirm_button, ("确定添加", 'confirm_button')).location_once_scrolled_into_view
        self.click_element(aloc.confirm_button, ("确定添加", 'confirm_button'))
        time.sleep(2)
        course_encoding = self.get_ele_text(aloc.course_encoding, ("获取课程编码", 'course_encoding'))
        course_title_add_done = self.get_ele_text(aloc.course_title_add_done, ("获取课程名称", 'course_title_add_done'))
        create_time = self.get_ele_text(aloc.create_time, ("获取创建时间", 'create_time'))

        return course_encoding, course_title_add_done, create_time

    def course_count(self):
        time.sleep(2)
        return int(self.get_ele_text(loc.count_str, ("课程数量", 'count_str'))[2: -2])

    def continue_to_add(self):
        self.click_element(aloc.continue_to_add_button, ("继续添加", 'continue_to_add_button'))

    def return_button(self):
        self.click_element(aloc.return_button, ("返回", 'return_button'))
        time.sleep(2)




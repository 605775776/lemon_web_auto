from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from Common.setting import Config


# 记录日志/失败截图+错误信息输出+抛出异常
class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待可见
    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        """

        :param loc:
        :param img_name:{页面名称_页面行为}
        :param timeout:
        :param poll_fre:
        :return:
        """
        logging.info("{}等待{}元素可见".format(img_name, loc))
        # 等待元素时长 等待开始的时间 记录下当前时间，等待结束的时间 记录下时间 求时间差
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            # 失败截图-写入日志
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise

    # 元素存在
    def wait_page_contain_element(self, loc, img_name, timeout=20, poll_fre=0.5):
        logging.info("{}等待{}元素存在".format(img_name, loc))
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(loc))
        except:
            # 失败截图-写入日志
            self.save_page_shot(img_name)
            logging.exception("页面元素不存在：")
            raise

    # 查找元素
    def get_element(self, loc, img_name):
        logging.info("在{}查找元素：{}".format(img_name, loc))
        try:
            ele = self.driver.find_element(*loc)

        except:
            self.save_page_shot(img_name)
            logging.exception("查找元素失败")
            raise
        else:
            return ele

    # 查找多个元素

    def get_elements(self, loc, img_name):
        logging.info("在{}查找所有匹配的元素：{}".format(img_name, loc))
        try:
            eles = self.driver.find_elements(*loc)

        except:
            self.save_page_shot(img_name)
            logging.exception("查找元素失败")
            raise
        else:
            return eles

    # 点击元素
    def click_element(self, loc, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        logging.info("在{}点击 {}元素".format(img_name, loc))

        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logging.exception("点击元素失败")
            raise

    # 元素的输入操作
    def input_text(self, loc, value, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        logging.info("在{}往 {}元素输入{}".format(img_name, loc, value))

        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logging.exception("元素输入文本失败")
            raise

    # 获取属性
    def get_ele_attribute(self, loc, attr_name, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        logging.info("在{}获取{}元素的{}属性".format(img_name, loc, attr_name))

        try:
            value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的属性失败")
            raise
        else:
            logging.info("属性值为{}".format(value))
            return value

    # 获取文本
    def get_ele_text(self, loc, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        logging.info("在{}获取{}元素的文本值".format(img_name, loc))

        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的文本失败")
            raise
        else:
            logging.info("文本值：{}".format(text))
            return text

    def save_page_shot(self, img_name):
        # 存储图片
        # 命名规范 页面名称_页面行为_时间.png
        # 文件完整名称 = Outputs的screenshots+页面名称_页面行为_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = Config.screenshot_dir + "/{}_{}.png".format(img_name, now)
        # file_name = "{}_{}.png".format(img_name, "当前时间")
        self.driver.save_screenshot(screenshot_path)
        logging.info("页面图片保存在：{}".format(screenshot_path))


if __name__ == '__main__':
    pass

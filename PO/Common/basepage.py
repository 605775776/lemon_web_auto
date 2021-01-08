from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待可见
    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        logging.info("{}等待{}元素可见".format(img_name, loc))
        # 等待元素时长 等待开始的时间 记录下当前时间，等待结束的时间 记录下时间 求时间差
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            # 失败截图-写入日志
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise
        else:
            # 时间差
            pass

    # 查找元素
    def get_element(self):
        pass

    # 点击
    def click_element(self):
        pass

    # 输入
    def input_text(self):
        pass

    # 获取属性
    def get_ele_attribute(self):
        pass

    # 获取文本
    def get_ele_text(self):
        pass

    def save_page_shot(self, img_name):
        # 存储图片
        # 命名规范 页面名称_页面行为_时间.png
        # 文件完整名称 = Outputs的screenshots+页面名称_页面行为_时间.png
        file_name = "{}_{}.png".format(img_name, "当前时间")
        self.driver.save_screenshot("图片存储路径" + img_name)
        logging.info("页面图片保存在：{}".format("图片存储路径" + img_name))


if __name__ == '__main__':
    pass

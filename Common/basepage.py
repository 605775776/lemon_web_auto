from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Common.logger_handler import logger
import time
from Common.setting import Config


# 记录日志/失败截图+错误信息输出+抛出异常
class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待可见
    def wait_ele_visible(self, loc, img_name_loc, timeout=20, poll_fre=0.5):
        """
        :param loc:
        :param img_name_loc:{页面名称_页面行为}
        :param timeout:
        :param poll_fre:
        :return:
        """
        logger.info("{}等待{}元素可见".format(img_name_loc[0], img_name_loc[1]))
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(loc))

        except:
            self.save_page_shot(img_name_loc[0])
            logger.exception("等待元素{}可见失败：".format(img_name_loc[1]))
            raise

    # 元素存在
    def wait_page_contain_element(self, loc, img_name_loc, timeout=20, poll_fre=0.5):
        logger.info("{}等待{}元素存在".format(img_name_loc[0], img_name_loc[1]))
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(loc))
        except:
            self.save_page_shot(img_name_loc[0])
            logger.exception("页面元素{}不存在：".format(img_name_loc[1]))
            raise

    # 查找元素
    def get_element(self, loc, img_name_loc):
        logger.info("在{}查找元素：{}".format(img_name_loc[0], img_name_loc[1]))
        try:
            ele = self.driver.find_element(*loc)
            # print(loc)
            # print("------")
            # print(*loc)
            # print("------")
            # print(ele)
        except:
            self.save_page_shot(img_name_loc[0])
            logger.exception("查找元素{}失败".format(img_name_loc[1]))
            raise
        else:
            return ele

    # 查找多个元素
    def get_elements(self, loc, img_name_loc):
        logger.info("在{}查找所有匹配的元素：{}".format(img_name_loc[0], img_name_loc[1]))
        try:
            eles = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(img_name_loc[0])
            logger.exception("查找元素{}失败".format(img_name_loc[1]))
            raise
        else:
            return eles

    # 点击元素
    def click_element(self, loc, img_name_loc, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name_loc, timeout, poll_fre)
        ele = self.get_element(loc, img_name_loc)
        logger.info("在{}点击 {}元素".format(img_name_loc[0], img_name_loc[1]))

        try:
            ele.click()
        except:
            self.save_page_shot(img_name_loc)
            logger.exception("点击元素{}失败".format(img_name_loc[1]))
            raise

    # 元素的输入操作
    def input_text(self, loc, value, img_name_loc, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name_loc, timeout, poll_fre)
        ele = self.get_element(loc, img_name_loc)
        logger.info("在{}往 {}元素输入{}".format(img_name_loc[0], img_name_loc[1], value))
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name_loc)
            logger.exception("元素输入{}文本失败".format(img_name_loc[1]))
            raise

    # 获取属性
    def get_ele_attribute(self, loc, attr_name, img_name_loc, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name_loc, timeout, poll_fre)
        ele = self.get_element(loc, img_name_loc)
        logger.info("在{}获取{}元素的{}属性".format(img_name_loc[0], img_name_loc[1], attr_name))
        try:
            value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name_loc)
            logger.exception("获取元素{}的属性失败".format(img_name_loc[1]))
            raise
        else:
            logger.info("属性值为{}".format(value))
            return value

    # 获取文本
    def get_ele_text(self, loc, img_name_loc, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name_loc, timeout, poll_fre)
        ele = self.get_element(loc, img_name_loc)
        logger.info("在{}获取{}元素的文本值".format(img_name_loc[0], img_name_loc[1]))
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name_loc)
            logger.exception("获取元素{}的文本失败".format(img_name_loc[1]))
            raise
        else:
            logger.info("元素{}的文本值：{}".format(img_name_loc[1], text))
            return text

    def save_page_shot(self, img_name):
        # 存储图片
        # 命名规范 页面名称_页面行为_时间.png
        # 文件完整名称 = Outputs的screenshots+页面名称_页面行为_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = Config.screenshot_dir + "\\{}_{}.png".format(img_name, now)
        print(screenshot_path)
        self.driver.save_screenshot(screenshot_path)
        logger.info("页面图片保存在：{}".format(screenshot_path))

    # 鼠标下滑点击
    # def mouse_move_down(self, loc, img_name_loc):
    #     ele = self.get_element(loc, img_name_loc)
    #
    #     ActionChains(self.driver).click(ele).perform()
    #     time.sleep(3)
    #     self.save_page_shot(1)
    #     logger.info("在{}点击{}元素".format(img_name_loc[0], img_name_loc[1]))
    #     try:
    #         ActionChains(self.driver).move_to_element_with_offset(ele, 0, 60).click().perform()
    #         time.sleep(3)
    #         logger.info("鼠标下移操作元素{}成功".format(img_name_loc[1]))
    #     except:
    #         logger.exception("鼠标点击元素{}下拉框失败".format(img_name_loc[1]))
    #         raise
    # 切换到新的窗口
    # iframe切换
    # alert切换
    # js执行 js语句 参数
    # 滚动条
    # 上传windows
    def switch_to_iframe(self, loc):
        # 等待
        try:
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            pass




if __name__ == '__main__':
    pass

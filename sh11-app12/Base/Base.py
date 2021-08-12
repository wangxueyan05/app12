from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, allure, os


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """

        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)
        :return:
        """
        self.get_element(loc).click()

    def send_element(self, loc, text):
        """
        输入文本
        :param loc: 元组 (By.ID,属性值) (By.CLASS_NAME,属性值) (By.XPATH,属性值)
        :param text: 输入框输入文本内容
        :return:
        """
        # 定位
        input_text = self.get_element(loc)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    @allure.step("滑动页面")
    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1:向上 2: 向下 3: 向左 4: 向右
        :return:
        """
        # 等待两秒
        time.sleep(2)
        # 屏幕分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 判断滑动方向
        if tag == 1:  # 向上
            allure.attach("滑动方向", "向上滑动")
            # 宽50% 高80% -> 高30%
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 2000)
        if tag == 2:  # 向下
            allure.attach("滑动方向", "向下滑动")
            # 宽50% 高30% -> 高80%
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 2000)
        if tag == 3:  # 向左
            allure.attach("滑动方向", "向左滑动")
            # 高50% 宽80% -> 宽30%
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 2000)
        if tag == 4:  # 向右
            allure.attach("滑动方向", "向右滑动")
            # 高50% 宽30% -> 宽80%
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 2000)

    @allure.step("获取toast消息")
    def get_toast(self, mess):
        """
        获取手机toast消息
        :param mess: xpath拼接语句
        :return:
        """
        # 获取提示消息
        message_xpath = (By.XPATH, "//*[contains(@text,'%s')]" % mess)

        # 获取文本
        toast_mess = self.get_element(message_xpath, timeout=3, poll_frequency=0.3).text

        allure.attach("获取结果", "%s" % toast_mess)

        return toast_mess

    @allure.step("截图操作")
    def screen(self, name="截图"):
        """截图"""
        # 截图名字
        image_name = "./Image" + os.sep + "%d.png" % int(time.time())
        # 截图
        self.driver.get_screenshot_as_file(image_name)

        with open(image_name, "rb") as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)  # 生成一个png附件

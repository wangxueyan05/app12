from Base.Base import Base
from Page.pageElements import PageElements
import allure


class PersonPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step("个人中心 获取我的收藏")
    def get_shoppingcart(self):
        """取我的收藏文本内容"""
        # 我的收藏文本
        res_text = self.get_element(PageElements.person_shoppingcart_id).text

        allure.attach("获取结果", "%s" % res_text)
        return res_text

    @allure.step("个人中心点击 设置")
    def click_setting_btn(self):
        """点击设置按钮"""

        self.click_element(PageElements.person_setting_btn_id)

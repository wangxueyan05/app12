from Base.Base import Base
from Page.pageElements import PageElements
import allure

class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step("首页点击我")
    def click_my_btn(self):
        """点击首页我"""

        self.click_element(PageElements.home_my_btn_id)

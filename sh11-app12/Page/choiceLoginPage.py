from Base.Base import Base
from Page.pageElements import PageElements
import allure


class ChoiceLoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step("登录选择页面 点击已有账号去登录")
    def click_exits_account(self):
        """登录选择页点击已有账号去登录"""
        self.click_element(PageElements.choice_login_exits_account_id)

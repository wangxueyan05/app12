from Page.homePage import HomePage
from Page.choiceLoginPage import ChoiceLoginPage
from Page.loginPage import LoginPage
from Page.personPage import PersonPage
from Page.settingPage import SettingPage
import allure


class Page:

    def __init__(self, driver):
        self.driver = driver


    def get_home_page(self):
        """返回首页对象"""
        return HomePage(self.driver)

    def get_choice_login_page(self):
        """返回选择登录页对象"""
        return ChoiceLoginPage(self.driver)

    def get_login_page(self):
        """返回登录页对象"""
        return LoginPage(self.driver)

    def get_person_page(self):
        """返回个人中心页对象"""
        return PersonPage(self.driver)

    def get_setting_page(self):
        """返回设置页对象"""
        return SettingPage(self.driver)

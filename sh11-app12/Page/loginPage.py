from Base.Base import Base
from Page.pageElements import PageElements
import allure


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step("登录操作")
    def login(self, account, passwd):
        """
        登录
        :param account: 账号
        :param passwd: 密码
        :return:
        """
        # 添加描述信息 -登录数据
        allure.attach("登录数据", "账号:%s 密码:%s" % (account, passwd))
        # 输入账号
        self.send_element(PageElements.login_account_id, account)
        # 输入密码
        self.send_element(PageElements.login_passwd_id, passwd)
        # 点击登录按钮
        self.click_element(PageElements.login_logon_btn_id)

    @allure.step("判断登录按钮是否存在")
    def if_login_btn(self):
        """
        判断登录按钮是否存在
        :return: 存在返回True 不存在返回False
        """
        try:
            # 登录按钮
            self.get_element(PageElements.login_logon_btn_id)
            allure.attach("结果", "存在")
            return True
        except:
            allure.attach("结果", "不存在")
            return False

    @allure.step("关闭登录页面")
    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(PageElements.login_close_btn_id)

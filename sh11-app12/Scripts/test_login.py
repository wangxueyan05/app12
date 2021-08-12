import sys, os, pytest

sys.path.append(os.getcwd())

from Base.getData import GetData
from Base.Page import Page

from Base.getDriver import get_android_driver

from selenium.common.exceptions import TimeoutException  # 导入超时异常


def data():
    """ {"suc":[()], "fail":[()]} """
    # 预期成功
    suc_list = []
    # 预期失败
    fail_list = []

    # 读yaml全部数据
    login_data = GetData().get_yml_data("login.yml")
    # 遍历数据
    for i in login_data.keys():
        # print("用例编号:", i)
        # print("用例编号值:", login_data.get(i))
        if login_data.get(i).get("toast"):  # case_num, name, pwd, toast, exp_data
            """预期失败"""
            fail_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd")
                              , login_data.get(i).get("toast"), login_data.get(i).get("exp_data")))
        else:  # case_num, name, pwd, exp_data
            """预期成功"""
            suc_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd")
                             , login_data.get(i).get("exp_data")))

    return {"suc": suc_list, "fail": fail_list}


class TestLogin:

    def setup_class(self):
        """初始化driver和统一入口类"""
        # 实例化driver
        self.driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 实例化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """关闭驱动对象"""
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def got_to_login(self):
        """进入登录页面，每个数据都需要依赖一次"""
        # 点击首页我
        self.page_obj.get_home_page().click_my_btn()
        # 点击选择登录页 已有账号去登录
        self.page_obj.get_choice_login_page().click_exits_account()

    def person_logout(self):
        """个人中心执行退出操作"""
        # 点击设置-描述
        # 点击设置
        self.page_obj.get_person_page().click_setting_btn()
        # 退出
        self.page_obj.get_setting_page().logout()

    @pytest.mark.parametrize("case_num, name, pwd, exp_data", data().get("suc"))
    def test_suc_login(self, case_num, name, pwd, exp_data):
        """
        预期成功用例
        :param case_num: 用例编号
        :param name: 用户名
        :param pwd: 密码
        :param exp_data: 预期结果
        :return:
        """
        # 登录
        self.page_obj.get_login_page().login(name, pwd)
        try:
            # 获取我的收藏
            result = self.page_obj.get_person_page().get_shoppingcart()
            try:
                # 断言
                assert result == exp_data
            except AssertionError:  # 断言失败异常
                # 截图
                self.page_obj.get_person_page().screen()
                # 断言失败 防止捕获断言异常 没有断言 那么测试方法默认断言通过
                assert False
            finally:
                # 退出
                self.person_logout()
        except TimeoutException:  # 超时异常 捕获没找到我的收藏
            # 截图
            self.page_obj.get_setting_page().screen()
            # if  # 登录按钮是否存在 :
            if self.page_obj.get_login_page().if_login_btn():
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()
            else:
                # 退出操作
                self.person_logout()
            assert False  # 捕获超时异常后 方法没有断言操作 默认通过

    @pytest.mark.parametrize("case_num, name, pwd, toast, exp_data", data().get("fail"))
    def test_fail_login(self, case_num, name, pwd, toast, exp_data):
        """
        预期失败测试用例
        :param case_num: 用例编号
        :param name: 用户名
        :param pwd: 密码
        :param toast: toast 消息拼接语句
        :param exp_data: 预期结果
        :return:
        """
        # 登录
        self.page_obj.get_login_page().login(name, pwd)
        try:
            # 获取toast消息
            message = self.page_obj.get_login_page().get_toast(toast)
            try:
                # 断言toast消息
                assert message == exp_data
            except AssertionError:
                # 截图
                self.page_obj.get_login_page().screen()
                assert False
        except TimeoutException:
            # 截图
            self.page_obj.get_login_page().screen()
            assert False
        finally:
            try:
                # 断言登录按钮
                assert self.page_obj.get_login_page().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_login_page().close_login_page()

            except AssertionError:
                # 截图
                self.page_obj.get_login_page().screen()
                # 退出
                self.person_logout()
                assert False
























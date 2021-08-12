from selenium.webdriver.common.by import By

from Base.Page import Page
from Base.getDriver import get_android_driver

# 声明driver
driver = get_android_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
# 实例化统一入口类
page = Page(driver)
# 点击我
page.get_home_page().click_my_btn()

# 点击已有账号去登录
page.get_choice_login_page().click_exits_account()

# 执行登录操作
page.get_login_page().login("13488834010", "159357")

# 获取提示消息
# message_xpath = (By.XPATH, "//*[contains(@text,'错误')]")
#
# # 定位获取文本
# message = page.get_setting_page().get_element(message_xpath, timeout=3, poll_frequency=0.3)
#
# print(message.text)

print(page.get_setting_page().get_toast("错误"))

# # 获取我的收藏
# print("个人中心获取文本:", page.get_person_page().get_shoppingcart())
#
# # 点击设置
# page.get_person_page().click_setting_btn()
#
# # 执行退出操作
# page.get_setting_page().logout()

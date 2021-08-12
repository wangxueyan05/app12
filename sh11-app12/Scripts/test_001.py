import allure, pytest


class Test001:

    def test_screen_shot(self):
        # 点击设置-描述
        # allure.attach("附件名字", "附件内容")  # 生成一个txt附件

        # allure.attach("附件名字", "附件内容", allure.attach_type.TEXT)  # 生成一个txt附件

        with open("./Image/123.png", "rb") as f:
            allure.attach("图片名字", f.read(), allure.attach_type.PNG)  # 生成一个png附件

        assert True


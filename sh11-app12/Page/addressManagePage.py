from Base.Base import Base
from Page.pageElements import PageElements


class AddressManagePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_edit_btn(self):
        """点击编辑按钮"""

        self.click_element(PageElements.address_manage_edit_btn_id)

    def click_modify_btn(self, name):
        """
        修改地址按钮
        :param name: 点击修改用户名
        :return: (By.XPATH, "//*[contains(@text,'%s')]/../following-sibling::*/*[contains(@text,'修改')]")
        """

        self.click_element((PageElements.address_manage_modify_btn_xpath[0],
                            PageElements.address_manage_modify_btn_xpath[1] % name))

    def click_delete_btn(self, name):
        """
        点击删除按钮
        :param name: 点击删除按钮的用户名
        :return:
        """
        self.click_element((PageElements.address_manage_delete_btn_xpath[0],
                            PageElements.address_manage_delete_btn_xpath[1] % name))

    def click_add_address_btn(self):
        """点击新增按钮"""
        self.click_element(PageElements.address_manage_add_address_btn_id)

    def get_name_phone(self):
        """
        返回地址管理列表所有用户名和手机号
        :return:
        """
        name_result = self.get_elements(PageElements.address_manage_name_phone_text_ids)

        return [i.text for i in name_result]

    def get_area(self):
        """
        返回地址管理列表所有所在地区
        :return:
        """
        area_result = self.get_elements(PageElements.address_manage_area_ids)

        return [i.text for i in area_result]

    def get_default_count(self):
        """
        返回默认数量
        :return:
        """
        return len(self.get_elements(PageElements.address_manage_default_btn_ids))

    def default_get_name_phone(self):
        """
        通过默认取用户名和手机号
        :return:
        """
        return self.get_element(PageElements.address_manage_default_get_name_phone_xpath).text

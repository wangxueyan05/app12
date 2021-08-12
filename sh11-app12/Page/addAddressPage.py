from Base.Base import Base
from Page.pageElements import PageElements


class AddAddressPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def add_address(self, name=None, phone=None, area=None, detail=None, code=None, isdefault=None):
        """
        添加新地址
        :param name: 收件人
        :param phone: 手机号
        :param area: 所在地区 ("省","市","区")
        :param detail: 详细地址
        :param code: 邮编
        :param isdefault: 设为默认地址
        :return:
        """
        # 收件人
        if name:
            self.send_element(PageElements.add_address_rec_name_id, name)
        # 手机号
        if phone:
            self.send_element(PageElements.add_address_rec_phone_id, phone)
        # 所在地区
        if area:
            self.click_element(PageElements.add_address_rec_area_id)
            # 省 (By.XPATH, "//*[contains(@text,'%s')]")
            self.click_element((PageElements.add_address_rec_select_province_xpath[0],
                                PageElements.add_address_rec_select_province_xpath[1] % area[0]))
            # 市
            self.click_element((PageElements.add_address_rec_select_city_xpath[0],
                                PageElements.add_address_rec_select_city_xpath[1] % area[1]))
            # 区
            if area[2]:
                self.click_element((PageElements.add_address_rec_select_area_xpath[0],
                                    PageElements.add_address_rec_select_area_xpath[1] % area[2]))
        # 详细地址
        if detail:
            self.send_element(PageElements.add_address_rec_detail_id, detail)
        # 邮编
        if code:
            self.send_element(PageElements.add_address_rec_post_code_id, code)
        # 设为默认
        if isdefault:
            self.click_element(PageElements.add_address_rec_default_id)

        # 保存
        self.click_element(PageElements.add_address_rec_save_id)

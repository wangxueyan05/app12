from selenium.webdriver.common.by import By


class PageElements:
    """首页"""
    # 我
    home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """登录选择页面"""
    # 已有账号去登录
    choice_login_exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页面"""
    # 账号
    login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_logon_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    # 关闭登录页面按钮
    login_close_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """个人中心页面"""
    # 我的收藏
    person_shoppingcart_id = (By.ID, "com.yunmall.lc:id/txt_my_shoppingcart")
    # 设置按钮
    person_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 确认退出按钮
    setting_logout_acc_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 取消退出按钮
    setting_logout_dis_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    # 地址管理
    setting_address_manage_id = (By.ID, "com.yunmall.lc:id/setting_address_manage")

    """地址管理页面"""
    # 编辑按钮
    address_manage_edit_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn")
    # 修改
    address_manage_modify_btn_xpath = (
        By.XPATH, "//*[contains(@text,'%s')]/../following-sibling::*/*[contains(@text,'修改')]")
    # 删除
    address_manage_delete_btn_xpath = (
        By.XPATH, "//*[contains(@text,'%s')]/../following-sibling::*/*[contains(@text,'删除')]")
    # 新增按钮
    address_manage_add_address_btn_id = (By.ID, "com.yunmall.lc:id/address_add_new_btn")
    # 用户名手机号 -一组
    address_manage_name_phone_text_ids = (By.ID, "com.yunmall.lc:id/receipt_name")
    # 所在地区 -一组
    address_manage_area_ids = (By.ID, "com.yunmall.lc:id/receipt_address")
    # 默认 -一组
    address_manage_default_btn_ids = (By.ID, "com.yunmall.lc:id/address_is_default")
    # 通过默认取用户名手机号
    address_manage_default_get_name_phone_xpath = (By.XPATH, "//*[contains(@text,'默认')]/../preceding-sibling::*")

    """新增地址页面"""
    # 收件人
    add_address_rec_name_id = (By.ID, "com.yunmall.lc:id/address_receipt_name")
    # 手机号
    add_address_rec_phone_id = (By.ID, "com.yunmall.lc:id/address_add_phone")
    # 所在地区
    add_address_rec_area_id = (By.ID, "com.yunmall.lc:id/address_province")
    # 所在地区-省
    add_address_rec_select_province_xpath = (By.XPATH, "//*[contains(@text,'%s')]")
    # 所在地区-市
    add_address_rec_select_city_xpath = (By.XPATH, "//*[contains(@text,'%s')]")
    # 所在地区-区
    add_address_rec_select_area_xpath = (By.XPATH, "//*[contains(@text,'%s')]")
    # 详细地址
    add_address_rec_detail_id = (By.ID, "com.yunmall.lc:id/address_detail_addr_info")
    # 邮编
    add_address_rec_post_code_id = (By.ID, "com.yunmall.lc:id/address_post_code")
    # 设为默认地址
    add_address_rec_default_id = (By.ID, "com.yunmall.lc:id/address_default")
    # 保存按钮
    add_address_rec_save_id = (By.ID, "com.yunmall.lc:id/button_send")

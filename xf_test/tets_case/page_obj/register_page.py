from xf_test.tets_case.page_obj.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep as s
from xf_test.tets_case.models.driver import driver_browser
from xf_test.tets_case.models.function import save_img


class RegisterPage(BasePage):
    """注册页面"""
    url = "/"

    # Action
    click_register_loc = (By.ID, "user_register")

    def click_register(self):
        """点击注册"""
        self.find_element(*self.click_register_loc).click()

    # Action
    send_username_loc = (By.ID, "id_username")
    send_pwd1_loc = (By.ID, "id_password1")
    send_pwd2_loc = (By.ID, "id_password2")
    register_button_loc = (By.XPATH, "/html/body/doctype/div/div[2]/form/button")

    def send_username(self, username):
        """注册用户名"""
        self.find_element(*self.send_username_loc).send_keys(username)

    def send_pwd1(self, pwd1):
        """注册输入密码"""
        self.find_element(*self.send_pwd1_loc).send_keys(pwd1)

    def send_pwd2(self, pwd2):
        """确认密码"""
        self.find_element(*self.send_pwd2_loc).send_keys(pwd2)

    def register_button(self):
        """注册按钮"""
        self.find_element(*self.register_button_loc).click()

    def user_register(self, usr, pwd1, pwd2):
        """用户注册"""
        self.open()
        self.click_register()
        self.send_username(usr)
        self.send_pwd1(pwd1)
        self.send_pwd2(pwd2)
        self.register_button()
        s(1)

    # Action
    register_usr_error_hint_loc = (By.XPATH, "/html/body/doctype/div/div[2]/form/ul[1]/li")
    register_pwd1_error_hint_loc = (By.XPATH, "/html/body/doctype/div/div[2]/form/ul[2]/li")
    register_pwd2_error_hint_loc = (By.XPATH, "/html/body/doctype/div/div[2]/form/ul[3]/li")
    register_success_loc = (By.ID, "wxf_logs_Name")

    def user_register_error_hint(self):
        """注册输入错误的提示"""
        return self.find_element(*self.register_usr_error_hint_loc).text,\
            self.find_element(*self.register_pwd1_error_hint_loc).text,\
            self.find_element(*self.register_pwd2_error_hint_loc).text

    def user_register_success(self):
        """用户注册成功"""
        return self.find_element(*self.register_success_loc).text


if __name__ == '__main__':
    driver = driver_browser()
    RegisterPage(selenium_driver=driver_browser()).user_register(usr='werwewq', pwd1='wxf990824', pwd2='wxf990824')
    assert RegisterPage(driver).register_usr_error_hint_loc, "已存在一位使用该名字的用户"
    save_img(driver, "register_index.png")
    driver.quit()

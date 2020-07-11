from selenium.webdriver.common.by import By
from xf_test.tets_case.page_obj.base_page import BasePage
from xf_test.tets_case.models.driver import driver_browser
from xf_test.tets_case.models.function import save_img
from time import sleep


class LoginPage(BasePage):
    """
    登录页面
    """
    url = '/'
    # Action
    log_click_login_loc = (By.ID, 'user_login')

    def log_click_login(self):
        """
        点击登陆
        :return:
        """
        self.find_element(*self.log_click_login_loc).click()

    login_username_loc = (By.ID, 'id_username')
    login_password_loc = (By.ID, 'id_password')
    login_button_loc = (By.XPATH, '//*[@class="btn btn-primary"]')

    def login_username(self, username):
        """
        登录用户名
        :param username:
        :return:
        """
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        """
        登录密码
        :param password:用户输入密码
        :return:None
        """
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        """
        登录按钮
        :return:None
        """
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username='www', password='wxf990824'):
        """
        定义统一登录入口，使用默认账号密码登录
        :param username:默认账号
        :param password:默认密码
        :return:None
        """
        self.open()
        self.log_click_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, '/html/body/div/div[2]/form/div[1]/text()')
    user_login_success_loc = (By.ID, "xfcust_Name")

    def user_error_login_hint(self):
        """
        用户登录错误提示
        :return:
        """
        return self.find_element(*self.user_error_hint_loc).text

    def user_login_success(self):
        """
        登录成功的用户名
        :return:
        """
        return self.find_element(*self.user_login_success_loc).text


if __name__ == '__main__':
    driver = driver_browser()
    LoginPage(selenium_driver=driver).user_login()
    save_img(driver, 'log_index.png')
    sleep(1)
    driver.quit()


class A(LoginPage):
    pass






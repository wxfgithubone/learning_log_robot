from time import sleep
import unittest, random
from xf_test.tets_case.models import myunit, function
from xf_test.tets_case.page_obj.login_page import LoginPage
from ddt import ddt, data


class LoginTest(myunit.MyTest):
    """学习日志登录测试用例"""

    def user_login_verify(self, username='', password=''):
        """
        测试用户登录
        """
        LoginPage(self.driver).user_login(username, password)

    @unittest.skip("跳过")
    def test_login1(self):
        """用户名正确，密码错误"""
        try:
            self.user_login_verify(username='www', password='123456')
            po = LoginPage(self.driver)
            self.assertEqual(po.user_error_login_hint(),
                             "Please enter a correct %(username)s and password. Note that both "
                             "fields may be case-sensitive.")
            function.save_img(self.driver, "pwd_error.png")
        except BaseException as f:
            print("用例1登录出错：{0}".format(f))
        else:
            print("用例1登录成功！")

    @unittest.skip("跳过")
    def test_login2(self):
        """用户名错误，密码正确"""
        self.user_login_verify(username='wer', password='wxf990824')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_error_login_hint(),
                         'Please enter a correct %(username)s and password. Note that both "'
                         '"fields may be case-sensitive.')
        function.save_img(self.driver, "user_error.png")

    @unittest.skip("跳过")
    def test_login3(self):
        """用户名密码为随机"""
        use = random.choice('zxcvbnmasdfghjkl')
        pwd = random.choice('asdfghjklqwer')
        username = 'www' + use
        password = 'wxf99' + pwd
        self.user_login_verify(username=username, password=password)
        po = LoginPage(self.driver)
        self.assertEqual(po.user_error_login_hint(),
                         'Please enter a correct %(username)s and password. Note that both "'
                         '"fields may be case-sensitive.')
        function.save_img(self.driver, "user_pwd_error.png")

    def test_login4(self):
        """用户名，密码正确"""
        try:
            self.user_login_verify(username='王小飞', password='wxf990824')
            sleep(1)
            po = LoginPage(self.driver)
            self.assertEqual(po.user_login_success(), 'Hello - {0} !'.format('小飞'))
        except BaseException as e:
            function.save_img(self.driver, "user_pwd_error.png")
            raise e
        else:
            print("登录成功！")


if __name__ == '__main__':
    unittest.main(verbosity=2)





















#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

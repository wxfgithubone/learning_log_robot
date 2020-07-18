import unittest, time
from xf_test.tets_case.models.myunit import MyTest
from xf_test.tets_case.page_obj.register_page import RegisterPage
from xf_test.tets_case.models.function import DoExcel, save_img, now_time
from ddt import ddt, data

list_data = DoExcel().read_data("F:/xf_py/conner/learning_log/xf_test/data/register.xlsx", 0)


@ddt
class RegisterTest(MyTest):
    """学习日志注册测试"""

    def user_register_verify(self, name='', pwd1='', pwd2=''):
        RegisterPage(self.driver).user_register(name, pwd1, pwd2)

    # @unittest.skip("跳过")
    @data(*list_data)
    def test_register1(self, arg):
        """参数化注册用户"""
        try:
            self.user_register_verify(name=arg['username'], pwd1=arg['password1'], pwd2=arg['password2'])
            re = RegisterPage(self.driver).user_register_success()
            self.assertEqual(re, 'Hello - {0} !'.format(arg['username']))
            print("%s注册成功！" % arg['username'])
            save_img(self.driver, 'register_success.png')
        except BaseException as f:
            print("register1执行失败：%s" % f)
        else:
            save_img(self.driver, 'register_error.png')
        finally:
            print(arg['username'] + "注册时间：%s" % now_time())


if __name__ == '__main__':
    unittest.main(verbosity=2)







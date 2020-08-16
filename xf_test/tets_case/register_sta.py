import unittest, time
from xf_test.tets_case.models.db import MyDB
from xf_test.tets_case.models.myunit import MyTest
from xf_test.tets_case.page_obj.register_page import RegisterPage
from xf_test.tets_case.models.function import DoExcel, save_img, now_time
from ddt import ddt, data

list_data = DoExcel("F:/xf_py/conner/learning_log_UI/xf_test/data/register.xlsx", 0).read_data()


@ddt
class RegisterTest(MyTest):
    """学习日志注册测试"""

    def user_register_verify(self, name='', pwd1='', pwd2=''):
        RegisterPage(self.driver).user_register(name, pwd1, pwd2)

    @unittest.skip("跳过")
    @data(*list_data)
    def test_register1(self, arg):
        """参数化注册用户"""
        try:
            self.user_register_verify(name=arg['username'], pwd1=arg['password1'], pwd2=arg['password2'])
            find_name = RegisterPage(self.driver).user_register_success()
            self.assertEqual(find_name, 'Hello - {0} !'.format(arg['username']))
        except BaseException as f:
            save_img(self.driver, 'register_error.png')
            raise f
        else:
            # save_img(self.driver, 'register_success.png')
            query_sql = MyDB().select_data("SELECT * FROM auth_user WHERE username='{0}'".format(arg['username']))
            if query_sql:
                print("\n{0}，注册成功！".format(arg['username']))
                MyDB().delete_data("DELETE FROM auth_user WHERE username='{0}'".format(arg['username']))
            else:
                raise ("{0}未找到".format(arg['username']))
        finally:
            print(arg['username'] + "  - 注册时间：%s" % now_time())


if __name__ == '__main__':
    unittest.main(verbosity=2)










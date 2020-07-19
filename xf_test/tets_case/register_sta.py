import unittest, time
from xf_test.tets_case.models.db import get_mysql
from xf_test.tets_case.models.myunit import MyTest
from xf_test.tets_case.page_obj.register_page import RegisterPage
from xf_test.tets_case.models.function import DoExcel, save_img, now_time
from ddt import ddt, data

list_data = DoExcel("../data/register.xlsx", 0).read_data()


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
            find_name = RegisterPage(self.driver).user_register_success()
            self.assertEqual(find_name, 'Hello - {0} !'.format(arg['username']))
            save_img(self.driver, 'register_success.png')
            try:
                query = "SELECT * FROM auth_user WHERE username='{0}'".format(arg['username'])
                user = get_mysql(sql=query)
                if user:
                    print("用户 - {0} - 注册成功，已在数据库中查询到！".format(arg['username']))
                else:
                    print("用户 - {0} - 未找到！！！".format(arg['username']))
            except Exception as e:
                print("数据库查询异常：%s" % e)
        except BaseException as f:
            print("register1执行失败：%s" % f)
            save_img(self.driver, 'register_error.png')
        else:
            print(arg['username'] + "  - 注册时间：%s" % now_time())
        finally:
            pass


if __name__ == '__main__':
    unittest.main(verbosity=2)







from xf_test.tets_case.models.function import WriteReport, now_time
from HTMLTestRunner import HTMLTestRunner
import unittest


if __name__ == '__main__':
    # filename = './xf_test/report/report/' + now_time() + 'result.html'  # 相对路径(移植性高)
    filename = r'F:\xf_py\conner\learning_log_UI\xf_test\report\report\\' + now_time() + 'result.html'  # 绝对路径（不易出错）
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='学习日志自动化测试报告',
                                description='环境：Windows 10 浏览器：Firefox、Chrome、IE、Opera',
                                tester='王小飞')
        try:
            discover = unittest.defaultTestLoader.\
                discover(r'F:\xf_py\conner\learning_log_UI\xf_test\tets_case', pattern='*_sta.py')  # ./xf_test/tets_case
            runner.run(discover)
        except BaseException as e:
            print("加载用例出错：{0}".format(e))
            raise e
        else:
            print("用例已全部加载完成！")

    f.close()

    op = WriteReport('F:\\xf_py\\conner\\learning_log_UI\\xf_test\\report\\report\\')
    file_path = op.new_report()  # ./xf_test/report/report/
    op.send_emil(file_path)












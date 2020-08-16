from xf_test.tets_case.models.function import WriteReport, now_time
from HTMLTestRunner import HTMLTestRunner
import unittest


if __name__ == '__main__':
    # filename = './xf_test/report/report/' + now_time() + 'result.html'  # 相对路径(移植性高)
    filename = 'F:\\xf_py\\conner\\learning_log_UI\\xf_test\\report\\report\\' + now_time() + 'result.html'  # 绝对路径（不易出错）
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title='学习日志自动化测试报告',
                            description='环境：Windows 10 浏览器：Firefox',
                            tester='王小飞')
    try:
        discover = unittest.defaultTestLoader.\
            discover('F:\\xf_py\\conner\\learning_log_UI\\xf_test\\tets_case', pattern='*_sta.py')  # ./xf_test/tets_case
        runner.run(discover)
    except BaseException as f:
        print("加载用例出错：{0}".format(f))
    else:
        print("用例已全部加载完成！")

    fp.close()
    op = WriteReport('F:\\xf_py\\conner\\learning_log_UI\\xf_test\\report\\report\\')
    file_path = op.new_report()  # ./xf_test/report/report/
    op.send_emil(file_path)












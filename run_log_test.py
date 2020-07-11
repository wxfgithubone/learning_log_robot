from xf_test.tets_case.models.function import send_emil, new_report, now_time
from HTMLTestRunner import HTMLTestRunner
import unittest
# def send_emil(file_new):
#     """=========定义发送邮件函数==========="""
#     f = open(file_new, 'rb')  # 打开文件
#     mail_body = f.read()  # 读取
#     f.close()  # 读取完关闭
#     sender = '1845719332@qq.com'  # 发送的邮箱
#     receiver = "652894729@qq.com"  # 接收邮箱
#     smtp_server = "smtp.qq.com"  # 发送邮箱服务器
#     username = "1845719332@qq.com"  # 发送邮箱用户/密码
#     password = "fqijzfeesegjbjbd"
#     msg = MIMEText(mail_body, 'html', 'utf-8')  # 邮件内容
#     msg['Subject'] = Header('自动化测试报告', 'utf-8')  # 主题
#     smtp = smtplib.SMTP_SSL(smtp_server, 465)  # 连接
#     smtp.login(username, password)
#     smtp.sendmail(sender, receiver, msg.as_string())  # 发送
#     smtp.quit()
#     print("邮件已发出！")

# def new_report(testreport):
#     """====查找最新的测试报告文件====="""
#     lists = os.listdir(testreport)
#     lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
#     file_new = os.path.join(testreport, lists[-1])
#     print(file_new)
#     return file_new


if __name__ == '__main__':
    # filename = './xf_test/report/report/' + now_time() + 'result.html'  # 相对路径
    filename = 'F:\\xf_py\\conner\\learning_log\\xf_test\\report\\report\\' + now_time() + 'result.html'  # 绝对路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title='学习日志自动化测试报告',
                            description='环境：Windows 10 浏览器：Firefox',
                            tester='王小飞')
    try:
        discover = unittest.defaultTestLoader.\
            discover('F:\\xf_py\\conner\\learning_log\\xf_test\\tets_case', pattern='*_sta.py')  # ./xf_test/tets_case
        runner.run(discover)
    except BaseException as f:
        print("加载用例出错：{0}".format(f))
    else:
        print("用例已全部加载完成！")

    fp.close()
    file_path = new_report('F:\\xf_py\\conner\\learning_log\\xf_test\\report\\report\\')  # ./xf_test/report/report/
    send_emil(file_path)


# print(sys.path)










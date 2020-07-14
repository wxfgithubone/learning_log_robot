import os, time, smtplib
from email.mime.text import MIMEText
from email.header import Header
from xf_test.tets_case.models.driver import driver_browser


def save_img(driver, img_name):
    """
    截图
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    now = time.strftime("%Y %m %d_%H %M %S_", time.localtime(time.time()))
    driver.get_screenshot_as_file(base_dir + "/report/image/" + now + img_name)


def send_emil(new_file):
    """
    发送邮件
    """
    f = open(new_file, "rb")
    mail_body = f.read()
    sender = '1845719332@qq.com'
    receiver = "652894729@qq.com"
    smtp_server = "smtp.qq.com"
    username = "1845719332@qq.com"
    password = "fqijzfeesegjbjbd"
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件已发出！")


def new_report(test_report):
    """
    查找最新文件
    """
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getatime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


def now_time():
    """
    获取当前时间
    """
    now = time.strftime("%Y_%m_%d %H-%M-%S ")
    return now


def read_excel():
    """
    读取excel
    """
    pass


if __name__ == '__main__':
    dr = driver_browser()
    dr.get('http://www.baidu.com')
    dr.find_element_by_id("kw").send_keys("selenium")
    dr.find_element_by_id("su").click()
    time.sleep(2)
    save_img(dr, "baidui.png")
    dr.quit()

























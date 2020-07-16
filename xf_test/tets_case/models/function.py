import os, time, smtplib, xlrd
from email.mime.text import MIMEText
from email.header import Header
from xf_test.tets_case.models.driver import driver_browser
# from openpyxl import load_workbook  # 兼容问题没用这个，要32位的，懒得装了


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
    password = "令牌密码"
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


class DoExcel(object):
    """读取excel"""
    def __init__(self, file_name=None, sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            self.file_name = \
                'F:/xf_py/conner/learning_log/xf_test/data/login.xlsx'  # 没有指定文件就使用该文件
            self.sheet_name = 0  # 默认第一个sheet

    def get_data(self):
        """获取sheet的内容"""
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_name]
        return tables

    def get_unit_nrows(self):
        """获取单元格行数"""
        tables = self.get_data()
        return tables.nrows

    def get_unit_ncols(self):
        """获取列数"""
        tables = self.get_data()
        return tables.ncols

    def get_unit_value(self, row, col):
        """获取单元格数据"""
        return self.get_data().cell_value(row, col)

    def get_all_data(self):
        """获取全部数据"""
        text_data = []
        for i in range(1, self.get_unit_nrows()):  # 1-文件最大行数 外层循环控制次数（多少行即循环多少次）
            for j in range(self.get_unit_ncols()):  # 最大列数  内层循环控制外层循环的行数+自己的列数
                text_data.append(self.get_unit_value(i, j))  # 每次追加第i行，第j列：1-0 1-1 1-2 1-3.....
        return text_data


if __name__ == '__main__':
    # dr = driver_browser()
    # dr.get('http://www.baidu.com')
    # dr.find_element_by_id("kw").send_keys("selenium")
    # dr.find_element_by_id("su").click()
    # time.sleep(2)
    # save_img(dr, "baidui.png")
    # dr.quit()
    op = DoExcel()
    print("文件的行数为：{0} 列数为：{1}".format(op.get_unit_nrows(), op.get_unit_ncols()))
    print("第一行第一列：%s" % op.get_unit_value(row=0, col=0))
    print("第一行第二列：%s" % op.get_unit_value(0, 1))
    print(op.get_all_data())




























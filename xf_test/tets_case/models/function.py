import os, time, smtplib, xlrd
from email.mime.text import MIMEText
from email.header import Header
from xf_test.tets_case.models.driver import driver_browser
# from openpyxl import load_workbook  # 兼容问题没用这个，要32位的，懒得装了


def now_time():
    """
    获取当前时间
    """
    now = time.strftime("%Y_%m_%d %H-%M-%S ")
    return now


def save_img(driver, img_name):
    """
    截图
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    driver.get_screenshot_as_file(base_dir + "/report/image/" + now_time() + img_name)


class WriteReport(object):
    """用于编写并发送测试报告的类"""
    def __init__(self, test_report, new_file=None):
        self.test_report = test_report
        self.new_file = new_file

    def new_report(self):
        """
        查找最新文件
        """
        lists = os.listdir(self.test_report)
        lists.sort(key=lambda fn: os.path.getatime(self.test_report + "\\" + fn))
        file_new = os.path.join(self.test_report, lists[-1])
        print(file_new)
        return file_new

    def send_emil(self, new_file):
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


class DoExcel(object):
    """读取excel"""
    def __init__(self, file_name=None, sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            self.file_name = \
                'F:/xf_py/conner/learning_log/xf_test/data/register.xlsx'  # 没有指定文件就使用该文件
            self.sheet_name = 0  # 默认第一个sheet

    def get_tab(self):
        """获取sheet的内容"""
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_name]
        return tables

    def get_unit_nrows(self):
        """获取单元格行数"""
        tables = self.get_tab()
        return tables.nrows

    def get_unit_ncols(self):
        """获取列数"""
        tables = self.get_tab()
        return tables.ncols

    def get_unit_value(self, row, col):
        """获取单元格数据"""
        return self.get_tab().cell_value(row, col)

    def read_data(self, file_name, sheet_index):
        """获取全部数据，dict类型"""
        data = xlrd.open_workbook(file_name)
        tab = data.sheets()[sheet_index]
        nrows = self.get_unit_nrows()  # 行数
        ncols = self.get_unit_ncols()  # 列数
        header = tab.row_values(0)  # 标题
        lists = []  # 创建一个空列表
        for x in range(1, nrows):  # 第一行为标题（第一行为0），所以从第二行开始
            row = tab.row_values(x)
            # print("\033[31m外层行循环：\033[0m %s" % x)
            if row:
                app = {}  # 创建空字典
                for y in range(ncols):
                    # print("\033[33m内层列循环：\033[0m %s" % y)
                    app[header[y]] = row[y]
                    # print("标题：{0} - 参数：{1}".format(header[y], row[y]))
                lists.append(app)
        return lists

    def write_data(self):
        """写入Excel"""
        pass


if __name__ == '__main__':
    # 参数化测试
    op = DoExcel()
    dr = driver_browser()
    list_data = op.read_data('../../data/login.xlsx', 0)
    for i in range(len(list_data)):
        dr.get('http://www.baidu.com')
        dr.find_element_by_id("kw").send_keys(list_data[i]["username"])
        dr.find_element_by_id("su").click()
        print(list_data[i]["username"])
        save_img(dr, "baidui.png")
        time.sleep(1)
    dr.quit()




























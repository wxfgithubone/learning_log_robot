from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """
    页面基础类，用于所有页面的继承
    """

    log_url = 'http://localhost:8000'

    def __init__(self, selenium_driver, base_url=log_url):
        """
        初始化驱动，地址等
        """
        self.driver = selenium_driver
        self.base_url = base_url

    def on_page(self, page_title):
        """
        返回页面的title
        """
        return page_title in self.driver.title

    def _open(self, url):
        """
        打开地址，最大化窗口
        """
        self.driver.get(url)
        self.driver.maximize_window()
        # self.driver.set_window_size(1920, 1080)

    def open(self):
        """
        调用_open方法
        """
        self._open(self.base_url)

    def find_element(self, *loc):
        """
        定位单个元素
        *loc任意数量的位置参数（带单个星号参数）
        """
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except BaseException as f:
            print("错误{0}\n元素未找到{1}".format(f, loc))

    def find_elements(self, *loc):
        """
        定位一组元素
        """
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_any_elements_located(loc))
            return self.driver.find_elements(*loc)
        except BaseException as f:
            print("错误{0}\n元素未找到{1}".format(f, loc))

    def script(self, src):
        """
        js代码编写
        """
        return self.driver.execute_script(src)

    def get_cookie(self):
        pass

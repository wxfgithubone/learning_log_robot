class BasePage(object):
    """
    页面基础类，用于所有页面的继承
    """

    log_url = 'http://localhost:8000'

    def __init__(self, selenium_driver, base_url=log_url):
        """
        初始化驱动，地址等
        :param selenium_driver:
        :param base_url:
        """
        self.driver = selenium_driver
        self.base_url = base_url

    def on_page(self, page_title):
        """
        返回页面的title
        :param page_title:
        :return:
        """
        return page_title in self.driver.title

    def _open(self, url):
        """
        打开地址，最大化窗口
        :param url:
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()
        # self.driver.set_window_size(1920, 1080)

    def open(self):
        """
        调用_open方法
        :return:
        """
        self._open(self.base_url)

    def find_element(self, *loc):
        """
        定位单个元素
        *loc任意数量的位置参数（带单个星号参数）
        :param loc:
        :return:
        """
        # try:
        #     WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
        #     return self.driver.find_element(*loc)
        # except BaseException as f:
        #     print("错误{0}\n元素未找到{1}".format(f, loc))
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        定位一组元素
        :param loc:
        :return:
        """
        # try:
        #     WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
        #     return self.driver.find_elements(*loc)
        # except BaseException as f:
        #     print("错误{0}\n元素未找到{1}".format(f, loc))
        return self.driver.find_elements(*loc)

    def script(self, src):
        """
        用于js代码的编写
        :param src:
        :return:
        """
        return self.driver.execute_script(src)







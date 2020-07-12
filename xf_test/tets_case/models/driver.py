from selenium.webdriver import Remote
from time import sleep
import warnings


def driver_browser():
    """配置浏览器驱动"""
    warnings.simplefilter("ignore", ResourceWarning)  # 消除警告
    lists = {
        'http://127.0.0.1:5555/wd/hub': 'firefox',
        'http://127.0.0.1:5556/wd/hub': 'chrome',
    }
    for host, browser in lists.items():
        # print(host, browser)
        driver = Remote(
            command_executor=host,
            desired_capabilities={'platform': 'ANY',
                                  'browserName': browser,
                                  'version': '',
                                  'javascriptEnabled': True
                                  }
        )
        return driver


if __name__ == '__main__':
    dr = driver_browser()
    dr.get("http://www.baidu.com")
    dr.maximize_window()
    sleep(2)
    dr.quit()


















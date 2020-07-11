from selenium.webdriver import Remote
from time import sleep
import warnings
from selenium import webdriver


# 启动浏览器的驱动
def driver_browser():
    # driver = webdriver.Firefox()
    warnings.simplefilter("ignore", ResourceWarning)
    lists = {
        'http://127.0.0.1:5555/wd/hub': 'firefox',
        # 'http://127.0.0.1:5556/wd/hub': 'chrome',
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


















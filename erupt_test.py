# Time：2020/8/18  Author：王哈哈
from xf_test.tets_case.models.function import now_time
from selenium import webdriver
from time import sleep
import multiprocessing


def erupt_bai_du(browser, search):
    print(f"开始时间：{now_time()}；浏览器：{browser}；搜索内容：{search}")
    if browser == 'chrome':
        driver = webdriver.Chrome(r"F:\xf_py\conner\learning_log_UI\driver\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie(r"F:\xf_py\conner\learning_log_UI\driver\IEDriverServer.exe")
    elif browser == 'opera':
        driver =webdriver.Opera()
    else:
        print("浏览器参数有误：{}".format(browser))
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    driver.close()


if __name__ == '__main__':
    dicts = {"chrome": "selenium", "firefox": "python", "ie": "requests", "opera": "王者荣耀"}
    threads = []
    for b, s in dicts.items():
        t = multiprocessing.Process(target=erupt_bai_du, args=(b, s))
        threads.append(t)
    for t in range(len(dicts)):
        threads[t].start()
    for t in range(len(dicts)):
        threads[t].join()
    print("结束时间：{}".format(now_time()))



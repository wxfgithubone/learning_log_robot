# 创建时间 2020/8/17
from threading import Thread
from selenium import webdriver
from time import sleep, ctime


def open_bai_du(browser, search):
    print("开始时间：{}".format(ctime()))
    print("浏览器：{}".format(browser))
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        print("浏览器参数有误，只能为Chrome、Firefox！")
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    lists = {'chrome': 'threading', 'firefox': 'python'}
    threads = []
    files = range(len(lists))

    for browser, search in lists.items():
        t = Thread(target=open_bai_du, args=(browser, search))
        threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print("结束时间：{}".format(ctime()))





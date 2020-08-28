# -*-coding:utf-8 -*-
import time, multiprocessing
from selenium.webdriver import Remote

# driver = Remote(command_executor="http://192.168.1.128:5555/wd/hub",
#                 desired_capabilities={
#                     'platform': 'ANY',
#                     'browserName': "chrome",
#                     'version': '',
#                     'javascriptEnabled': True})
#
# driver.get('https://www.baidu.com')
# time.sleep(2)
# driver.quit()


def test_rc(host, browser):
    print(f'开始时间：{time.strftime("%Y_%m_%d %H-%M-%S ")}')
    print(f"IP:{host};浏览器：{browser}")
    driver = Remote(
        command_executor=host,
        desired_capabilities={
            'platform': 'ANY',
            'browserName': browser,
            'version': '',
            'javascriptEnabled': True
        }
    )
    driver.get('https://www.baidu.com')
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    start_time = time.perf_counter()
    lists = {
        'http://192.168.1.128:5555/wd/hub': 'chrome',  # 远程节点
        'http://127.0.0.1:5556/wd/hub': 'chrome',  # 本机节点
    }
    threads = []
    for h, b in lists.items():
        t = multiprocessing.Process(target=test_rc, args=(h, b))
        threads.append(t)

    for t in range(len(lists)):
        threads[t].start()

    for t in range(len(lists)):
        threads[t].join()

    print(f'结束时间：{time.strftime("%Y_%m_%d %H-%M-%S ")}')
    print(f"程序运行时间：{time.perf_counter() - start_time}")




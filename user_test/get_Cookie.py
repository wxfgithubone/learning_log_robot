import json
import traceback
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from xf_test.tets_case.models.function import save_img
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


# 启用谷歌无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')


def write_cookie():
    """登录后将session写入json文件"""
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://localhost:8000/users/login/')
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('id_username').send_keys('wxf')
        driver.find_element_by_id('id_password').send_keys('wxf990824')
    except NoSuchElementException as e:
        print(f'错误：{e}')
        traceback.print_exc()
    else:
        element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.NAME, "submit")))
        element.click()
        save_img(driver, '无头模式获取session截图.png')
        cookie_data = []
        cookie = driver.get_cookies()
        cookie_data.append(cookie[0])
        json_cookie = json.dumps(cookie_data)
        with open('cookie.json', 'w+') as f:
            f.write(json_cookie)
        f.close()
    finally:
        pass


def login_cookie():
    """测试cookie"""
    driver1 = webdriver.Chrome(chrome_options=chrome_options)
    driver1.maximize_window()
    driver1.get('http://localhost:8000')
    with open('cookie.json', 'r', encoding='utf-8') as f:
        list_cookie = json.loads(f.read())
    for cookie1 in list_cookie:
        driver1.add_cookie({"name": cookie1['name'], "value": cookie1['value']})
    driver1.refresh()
    sleep(2)
    driver1.find_element_by_id('my_student').click()
    save_img(driver1, '无头模式测试session登录截图.png')
    sleep(3)
    f.close()


def user_cookie():
    """返回session"""
    with open('cookie.json', 'r', encoding='utf-8') as f:
        list_cookie = json.loads(f.read())
    for cookie2 in list_cookie:
        return {"name": cookie2['name'], "value": cookie2['value']}
    f.close()


if __name__ == '__main__':
    # print(user_cookie())
    # login_cookie()
    write_cookie()






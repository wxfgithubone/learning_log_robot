from selenium import webdriver
from user_test.get_Cookie import user_cookie
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:8000')
driver.implicitly_wait(15)
driver.maximize_window()
driver.add_cookie(user_cookie())
driver.refresh()
driver.find_element_by_id('index').click()
# 获得当前(主页)窗口句柄
index_windows = driver.current_window_handle
print(f"主页窗口句柄：{index_windows}")
driver.find_element_by_xpath('/html/body/doctype/div/div[2]/h4/a[5]').click()
# 获得所有窗口句柄
all_windows = driver.window_handles
print(f"所有窗口句柄：{all_windows}")
sleep(1)
driver.switch_to_window(all_windows[1])
sleep(1)
driver.switch_to_window(all_windows[0])
sleep(1)
driver.switch_to_window(all_windows[1])
sleep(3)












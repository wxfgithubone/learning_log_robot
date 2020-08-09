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
# 切换到iframe（id = "if"）
driver.switch_to.frame("if")
# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.switch_to.parent_frame()  # 该方法默认对应于离它最近的switch_to.frame（）方法 还可以通过switch_to.default_content（）跳回最外层的页面
sleep(3)








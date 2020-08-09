from selenium import webdriver
from user_test.get_Cookie import user_cookie
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('http://localhost:8000')
# driver.maximize_window()
driver.add_cookie(user_cookie())
driver.refresh()
# driver.find_element_by_id('my_img').click()
# driver.find_element_by_id('6').click()
# driver.find_element_by_name('name').send_keys('UI自动化添加,send_keys实现')
# #  send_keys上传
# driver.find_element_by_name('headimg').send_keys(r'F:\xf_py\conner\learning_log_UI\xf_test\data\img\2023186.jpg')
# driver.find_element_by_xpath('/html/body/doctype/div/div[2]/form/input[2]').click()
# driver.back()
# sleep(2)
"""
text：返回警告框中的文字信息
accept：接受现有警告框  # （谐音：a铺赛可特）
dismiss：取消现有警告框
send_keys：发送文本到警告框
"""
# driver.switch_to.alert.accept()  # 接受警告框
driver.find_element_by_id('my_img').click()
driver.find_element_by_id('6').click()
driver.find_element_by_name('name').send_keys('UI自动化添加,autoIT+js实现')
# js 实现点击
sleep(2)
js = 'document.getElementById("id_headimg").click();'
driver.execute_script(js)
# AutoIt (谐音：阿斗a特）
sleep(2)
os.system(r'F:\xf_py\conner\learning_log_UI\xf_test\data\img\img.exe')
sleep(2)
driver.find_element_by_xpath('//*[@value="提交"]').click()
driver.back()
sleep(2)
driver.switch_to.alert.accept()
driver.find_element_by_id('my_img').click()
sleep(3)
driver.quit()







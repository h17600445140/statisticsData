from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://fsscysc.csztessc.com.cn:8085/login")
driver.maximize_window()

driver.find_element_by_id('loginKey').send_keys('hc3')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('login').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/p[2]').click()
sleep(2)
print(driver.current_window_handle)
driver.find_element_by_xpath('//*[@id="app"]/section/header/div[2]/ul/li[4]').click()
print(driver.current_window_handle)
print(driver.window_handles)
win = driver.window_handles
driver.switch_to.window(win[1])
print(driver.current_window_handle)
driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[2]/div').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]').click()
sleep(2)
win = driver.window_handles
driver.switch_to.window(win[2])
driver.find_element_by_xpath('//*[@id="apportion.0.projectId"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="apportion.0.projectId"]').click()
driver.find_element_by_xpath('//*[@id="apportion.0.projectId.table"]/div/div/div[1]/div[3]/table').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="submit"]').click()


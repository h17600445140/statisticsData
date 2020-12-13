from time import sleep

from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('User-Agent={}'.format(UserAgent().chrome))
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.tapd.cn/cloud_logins/login")
driver.maximize_window()

driver.find_element_by_id("username").send_keys("17600445140")
driver.find_element_by_id("password_input").send_keys("Hc17600445140")
driver.find_element_by_xpath('//*[@id="tcloud_login_button"]').click()

driver.get("https://www.tapd.cn/67410840/bugtrace/bugreports/my_view")
print(driver.page_source)

num = 1
while True:
    print('第' + str(num) + "页----------------------------------------------")
    num += 1
    sleep(1)
    html = driver.page_source

    bug_title = driver.find_elements_by_xpath('//a[@class="editable-value j-bug-title-link namecol"]')
    severity = driver.find_elements_by_xpath('//span[@class="editable-value no-dropdown-arrow"]')
    for bug_title, severity in zip(bug_title, severity):
        print(bug_title.text, ":", severity.text)
    if driver.page_source.find('page-next') != -1:
        driver.find_element_by_xpath('//span[@class="page-btn page-next"]').click()
    else:
        break
driver.quit()


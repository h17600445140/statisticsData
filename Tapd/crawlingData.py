
def crawlingData(driver):
    driver.get("https://www.tapd.cn/cloud_logins/login")
    driver.maximize_window()

    driver.find_element_by_id("username").send_keys("17600445140")
    driver.find_element_by_id("password_input").send_keys("Hc17600445140")
    driver.find_element_by_xpath('//*[@id="tcloud_login_button"]').click()

    driver.get("https://www.tapd.cn/67410840/bugtrace/bugreports/my_view")

    data_list = []

    while True:
        driver.implicitly_wait(1)
        bug_title = driver.find_elements_by_xpath('//a[@class="editable-value j-bug-title-link namecol"]')
        version = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[4]')
        severity = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[5]')
        priority = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[6]')
        state = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[7]')
        handler = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[8]')
        creator = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[9]')
        bug_createTime = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[10]')
        bug_closeTime = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[11]')
        bug_solveTime = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[12]')
        bug_verificationTime = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[13]')
        fixPeople = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[14]')

        for bug_title, version, severity, priority, state, handler, creator, bug_createTime, bug_closeTime, bug_solveTime, bug_verificationTime, fixPeople in zip(bug_title, version, severity, priority, state, handler, creator, bug_createTime, bug_closeTime, bug_solveTime, bug_verificationTime, fixPeople):
            data_list.append({"bug标题":bug_title.text, "发现版本":version.text, "严重程度":severity.text, "优先级":priority.text, "状态":state.text, "处理人":handler.text.split(';')[0], "创建人":creator.text.strip(),
                              "创建时间":bug_createTime.text.split(' ')[0], "关闭时间":bug_closeTime.text.split(' ')[0], "解决时间":bug_solveTime.text.split(' ')[0], "验证时间":bug_verificationTime.text.split(' ')[0], "修复人":fixPeople.text.strip()})
        if len(driver.find_elements_by_xpath('//div[@id="simple_pager_div"]/span[2]/a')) != 0:
            driver.find_element_by_xpath('//span[@class="page-btn page-next"]').click()
        else:
            break

    return data_list








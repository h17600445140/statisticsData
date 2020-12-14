from time import sleep, strftime, localtime, time

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

creator_names = []
data_list = []
num = 1
while True:
    print('第' + str(num) + "页----------------------------------------------")
    num += 1
    sleep(1)
    html = driver.page_source
    bug_title = driver.find_elements_by_xpath('//a[@class="editable-value j-bug-title-link namecol"]')
    severity = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[5]')
    priority = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[6]')
    state = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[7]')
    handler = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[8]')
    creator = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[9]')
    createTime = driver.find_elements_by_xpath('//*[@id="bug_list_content"]/tbody/tr/td[10]')
    n = 0
    for bug_title, severity, priority, state, handler, creator, createTime in zip(bug_title, severity, priority, state, handler, creator, createTime):
        n= n+1
        if creator.text not in creator_names:
            creator_names.append(creator.text)
        print(n,":", bug_title.text, ":", severity.text, ":", priority.text, ":", state.text, ":", handler.text, ":", creator.text, ":", createTime.text)
        data_list.append({"bug标题":bug_title.text, "严重程度":severity.text, "优先级":priority.text, "状态":state.text, "处理人":handler.text, "创建人":creator.text, "创建时间":createTime.text.split(' ')[0]})
    if len(driver.find_elements_by_xpath('//div[@id="simple_pager_div"]/span[2]/a')) != 0:
        driver.find_element_by_xpath('//span[@class="page-btn page-next"]').click()
    else:
        break
driver.quit()
print(creator_names)
print(data_list)


def getdateNum(my_datas, dict) -> int:
    dict_len = len(dict)
    key = [key for key in dict.keys()]
    value = [value for value in dict.values()]
    result = []

    for dict in my_datas:
        for i in range(dict_len):
            if dict[key[i]] != value[i]:
                break
            if i == dict_len - 1 and dict[key[i]] == value[i]:
                result.append(list)
    result_len = len(result)
    return result_len

today = strftime("%Y-%m-%d", localtime(time()))
dict = [{"创建人":creator_name, "创建时间":today} for creator_name in creator_names]
print(dict)


for x in dict:
    num = getdateNum(data_list,x)
    print(x["创建人"]," 今日提交BUG数为"," :{}".format(num))




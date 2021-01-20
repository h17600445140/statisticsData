#-*-coding:utf-8-*-
import json
import math
import os

import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from time import localtime, strftime, time
from Tapd.crawlingData import crawlingData
from Tapd.createHtml import createHtml
from Tapd.screenshot import createPng
from Tapd.sendMessage import sendPNGMessage
from Tapd.utils import getdateNum


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('User-Agent={}'.format(UserAgent().chrome))
driver = webdriver.Chrome(options=chrome_options)


def draw_chart(dict, label_name, y_name, title, path):
    # 解决plt画图中文不能显示的问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 数据初始化
    labels = []
    bugs_data = []
    for key,value in dict.items():
        labels.append(key)
        bugs_data.append(int(value))

    x = np.arange(len(labels))  # the label locations

    # 动态修改y
    num = max([int(num) for num in dict.values()])
    num = math.ceil(num/10)*10+20
    if num>100:
        y = np.arange(0, num+10, 20)
    else:
        y = np.arange(0, num, 10)

    # fig：
    # ax：图表内容对象
    fig, ax = plt.subplots()

    # width：柱状图的宽度
    bar_width = 0.5
    # 画柱状图
    Bar_chart = ax.bar(x, bugs_data, bar_width, label=label_name, color='#87CEFA',zorder=5)

     # 增加标签（x,y,title）
    ax.set_yticks(y)
    ax.set_ylabel(y_name)      # bug_data
    ax.set_title(title)        # "每日新增bug数"
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # 为柱状图添加数据标签
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 点垂直偏移指数
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(Bar_chart)
    fig.tight_layout()
    plt.grid(axis='y')

    if len(x) > 6:
        plt.xticks(rotation=315)

    # 保存图片
    plt.savefig(path, bbox_inches='tight')
    plt.show()


def draw(list, dict, my_datas, version):
    # 每日新增BUG数
    dict1 = {i:getdateNum(my_datas, {"创建时间": i, '发现版本': version}) for i in list}
    draw_chart(dict1, 'bugs', 'bug_datas', '每日新增bug数', './png/每日新增bug数.png')

    # 每日待修复BUG数
    draw_chart(dict, 'bugs', 'bug_datas', '每日待修复BUG数', './png/每日待修复BUG数.png')

    # 每日已解决BUG数
    dict3 = {i: getdateNum(my_datas, {"解决时间": i, '发现版本': version}) for i in list}
    draw_chart(dict3, 'bugs', 'bug_datas', '每日解决bug数', './png/每日解决bug数.png')

    # 每日关闭BUG数
    dict4 = {i: getdateNum(my_datas, {"关闭时间": i, '发现版本': version}) for i in list}
    draw_chart(dict4, 'bugs', 'bug_datas', '每日关闭bug数', './png/每日关闭bug数.png')


def statisticsDta(my_datas,today,version) -> int:
    print("每日新增BUG数：{}".format(getdateNum(my_datas, {"创建时间": today, '发现版本': version})))
    print("每日解决BUG数：{}".format(getdateNum(my_datas, {"解决时间": today, '发现版本': version})))
    print("每日关闭BUG数：{}".format(getdateNum(my_datas, {"关闭时间": today, '发现版本': version})))
    resolvedBUG = getdateNum(my_datas, {"状态": '新', '发现版本': version}) + getdateNum(my_datas, {"状态": '接受/处理', '发现版本': version}) + getdateNum(my_datas, {"状态": '重新打开', '发现版本': version})
    print("每日待修复BUG数：{}".format(resolvedBUG))
    activation_bugs = resolvedBUG

    return activation_bugs


def testerData(my_datas, person, today, version):
    testerListData = []
    submit_bugs = getdateNum(my_datas, {"创建时间": today, '创建人': person, '发现版本': version})
    verified_bugs = getdateNum(my_datas, {"状态": "已解决", '处理人': person, '发现版本': version})
    close_bugs = getdateNum(my_datas, {"关闭时间": today, '创建人': person, '发现版本': version})
    testerListData.append(person)
    testerListData.append(str(submit_bugs))
    testerListData.append(str(verified_bugs))
    testerListData.append(str(close_bugs))
    return testerListData,submit_bugs,verified_bugs,close_bugs

def developerData(my_datas, person, today, version):
    developerListData = []
    solved_bugs = getdateNum(my_datas, {"解决时间": today, '修复人': person, '发现版本': version})
    surplus_bugs = getdateNum(my_datas, {"状态": "新", '处理人': person, '发现版本': version}) + getdateNum(my_datas, {"状态": "接受/处理", '处理人': person, '发现版本': version}) + getdateNum(my_datas, {"状态": "重新打开", '处理人': person, '发现版本': version})
    developer_todayBugs = getdateNum(my_datas, {"创建时间": today, "状态": "新", '处理人': person, '发现版本': version}) \
                          + getdateNum(my_datas, {"创建时间": today, "状态": "接受/处理", '处理人': person, '发现版本': version})  \
                          + getdateNum(my_datas, {"创建时间": today, "状态": "重新打开", '处理人': person, '发现版本': version}) \
                          + getdateNum(my_datas, {"创建时间": today, "状态": "已解决", '修复人': person, '发现版本': version}) \
                          + getdateNum(my_datas, {"创建时间": today, "状态": "已关闭", '修复人': person, '发现版本': version}) \
                          + getdateNum(my_datas, {"创建时间": today, "状态": "已验证", '修复人': person, '发现版本': version})

    developerListData.append(person)
    developerListData.append(str(solved_bugs))
    developerListData.append(str(surplus_bugs))
    developerListData.append(str(developer_todayBugs))
    return developerListData, solved_bugs, surplus_bugs, developer_todayBugs


if __name__ == '__main__':
    # 脚本初始化(注意：首次执行需要清空record.json文件)
    version = '2.1.7'
    username = '17600445140'
    password = 'Hc17600445140'
    # roboturl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a7d6ff37-bcf2-49d0-9f2c-dee68ec82e05'
    roboturl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9607d7b2-6c72-4e73-ae7a-e27c0990b467'
    developer = ["沈滔", "吴吉", "孙运", "李星", "李雄", "张科君", "尹君", "曾俊"]
    tester = ["伍洋", "苏林子", "刘巧利", "文玉婷", "唐洁TangJie01"]


    today = strftime("%Y-%m-%d", localtime(time()))

    my_datas = crawlingData(driver,version,username,password)

    # 统计总数居 -> 返回当日激活BUG数
    activation_bugs = statisticsDta(my_datas,today,version)

    # 读取记录文件
    with open("record.json", "r", encoding="UTF-8") as f:
        Rdata = json.load(f)
    Rdata["data"].update({today : str(activation_bugs)})

    data = Rdata

    # 写入记录文件
    with open("record.json", "w", encoding="UTF-8") as f:
        json.dump(data, f)

    list = [key for key in data["data"].keys()]
    # activation_bugs
    dict = data["data"]

    draw(list, dict, my_datas, version)

    testerTotalSubmit_bugs = 0
    testerTotalverified_bugs = 0
    testerTotalclose_bugs = 0
    # 测试
    testerTotalData = []
    for person in tester:
        testerListData,submit_bugs,verified_bugs,close_bugs = testerData(my_datas, person, today, version)
        testerTotalSubmit_bugs = testerTotalSubmit_bugs + submit_bugs
        testerTotalverified_bugs = testerTotalverified_bugs + verified_bugs
        testerTotalclose_bugs = testerTotalclose_bugs + close_bugs
        testerTotalData.append(testerListData)
    testerTotalData.append(["总计",str(testerTotalSubmit_bugs),str(testerTotalverified_bugs),str(testerTotalclose_bugs)])

    Title = (('测试人员', '今日提交BUG数', '待验证BUG数', '今日关闭BUG数'),)
    tester_html = 'testerHtml.html'
    createHtml(Title, testerTotalData, tester_html)

    html_path = os.path.realpath("html/testerHtml.html")
    screenshot_path = "./png/test.png"
    testerPNG_path = './png/tester.png'
    createPng(driver, html_path, screenshot_path, testerPNG_path)

    developerTotalSolved_bugs = 0
    developerTotalSurplus_bugs = 0
    developerTotalDeveloper_todayBugs = 0
    # 开发
    developerTotalData = []
    for person in developer:
        developerListData, solved_bugs, surplus_bugs, developer_todayBugs = developerData(my_datas, person, today, version)
        developerTotalSolved_bugs = developerTotalSolved_bugs + solved_bugs
        developerTotalSurplus_bugs = developerTotalSurplus_bugs + surplus_bugs
        developerTotalDeveloper_todayBugs = developerTotalDeveloper_todayBugs + developer_todayBugs
        developerTotalData.append(developerListData)
    developerTotalData.append(["总计", str(developerTotalSolved_bugs), str(developerTotalSurplus_bugs), str(developerTotalDeveloper_todayBugs)])

    Title = (('开发人员', '今日解决BUG数', '待解决BUG数', '今日新增bug数'),)
    developer_html = 'developerHtml.html'
    createHtml(Title, developerTotalData, developer_html)

    html_path = os.path.realpath("html/developerHtml.html")
    screenshot_path = "./png/develop.png"
    developPNG_path = './png/developer.png'
    createPng(driver, html_path, screenshot_path, developPNG_path)

    todayCloseBug = './png/每日关闭bug数.png'
    todayFixedBug = './png/每日待修复BUG数.png'
    todayAddBug = './png/每日新增bug数.png'
    todaySolvedBug = './png/每日解决bug数.png'

    sendPNGMessage(testerPNG_path,roboturl)
    sendPNGMessage(developPNG_path,roboturl)
    sendPNGMessage(todayCloseBug,roboturl)
    sendPNGMessage(todayFixedBug,roboturl)
    sendPNGMessage(todayAddBug,roboturl)
    sendPNGMessage(todaySolvedBug,roboturl)

    driver.quit()






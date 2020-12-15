#-*-coding:utf-8-*-
from time import localtime, strftime, time
from prettytable import PrettyTable

import matplotlib.pyplot as plt
import numpy as np
import math
import csv

# 脚本统计数据

# 获取数据
def getDatas(path) -> list:
    with open (path, newline='', encoding="UTF-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        my_datas = [data for data in spamreader]
    return my_datas

# 获取下标
def getIndex(my_datas, str) -> int:
    index = my_datas[0].index(str)
    return index

def getdateNum(my_datas, dict) -> int:
    dict_len = len(dict)
    str = [key for key in dict.keys()]
    key = [getIndex(my_datas, str) for str in str]
    value = [value for value in dict.values()]
    result = []

    for list in my_datas:
        for i in range(dict_len):
            if list[key[i]] != value[i]:
                break
            if i == dict_len-1 and list[key[i]] == value[i]:
                result.append(list)
    result_len = len(result)
    return result_len


def statisticsDta(my_datas,today) -> int:
    print("每日新增BUG数：{}".format(getdateNum(my_datas, {"创建日期": today})))
    print("每日待修复BUG数：{}".format(getdateNum(my_datas, {"Bug状态": '激活'})))
    activation_bugs = getdateNum(my_datas, {"Bug状态": '激活'})
    print("每日已解决BUG数：{}".format(getdateNum(my_datas, {"解决日期": today})))
    print("每日关闭BUG数：{}".format(getdateNum(my_datas, {"关闭日期": today})))
    return activation_bugs


def draw_chart(dict, label_name, y_name, title, path):
    # 解决plt画图中文不能显示的问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 数据初始化
    labels = []
    bugs_data = []
    for key,value in dict.items():
        labels.append(key)
        bugs_data.append(value)

    x = np.arange(len(labels))  # the label locations

    # 动态修改y
    num = max([num for num in dict.values()])
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
    plt.savefig(path)
    plt.show()

def statisticsData(my_datas, developer, tester, today):
    developer = developer
    developer_list1 = [{'指派给': i, 'Bug状态': '激活'} for i in developer]
    developer_list2 = [{'解决者': i, "解决日期": today} for i in developer]
    developer_dict1 = {}
    developer_dict2 = {}
    # 待解决BUG数
    # print('———————————————————— 待解决BUG数 ————————————————————')
    for i in developer_list1:
        num = getdateNum(my_datas, i)
        # print("{} 待解决BUG数为：{}".format(i['指派给'],num))
        developer_dict1.update({i['指派给']: num})

    # 今日解决BUG数
    # print('———————————————————— 今日解决BUG数 ————————————————————')
    for i in developer_list2:
        num = getdateNum(my_datas, i)
        # print("{} 今日解决BUG数为：{}".format(i['解决者'],num))
        developer_dict2.update({i['解决者']: num})

    y = PrettyTable(["开发人员", "待解决BUG数", "今日解决BUG数"])
    for i in range(len(developer)):
        list = []
        list.append(developer[i])
        list.append(developer_dict1[developer[i]])
        list.append(developer_dict2[developer[i]])
        y.add_row(list)
    print(y)

    # tester = ['由谁创建', '潘静', '王庆宁', '罗闪', '贾真', '袁妙妙', '苏林子', '黄超', '张友吉', '伍洋', '刘娟', '梅端倪', '曹雨荷', '丁蓓蓓', '李仁', '邓日业', '刘海霞', '朱双平', '冷梅', '王清', '杨玲', '曾彤芳', '曾光彬', '陈旭', '张锐', '肖城', '刘志成', '温春梅', '刘超', '阮荣', '陈湘娜', '董文静', '任佳乐', '陈高峰', '唐杰康', '赵钰铭', '张哲', '程林珊']
    tester = tester
    tester_list1 = [{'由谁创建': i, "创建日期": today} for i in tester]
    tester_list2 = [{'由谁创建': i, "关闭日期": today} for i in tester]
    tester_list3 = [{'指派给': i, "Bug状态": '已解决'} for i in tester]
    tester_dict1 = {}
    tester_dict2 = {}
    tester_dict3 = {}
    # 提交BUG数
    # print('———————————————————— 提交BUG数 ————————————————————')
    for i in tester_list1:
        num = getdateNum(my_datas, i)
        # print("{} 今天提交BUG数为：{}".format(i['由谁创建'],num))
        tester_dict1.update({i['由谁创建']: num})

    # 关闭BUG数
    # print('———————————————————— 关闭BUG数 ————————————————————')
    for i in tester_list2:
        num = getdateNum(my_datas, i)
        # print("{} 今天关闭BUG数为：{}".format(i['由谁创建'],num))
        tester_dict2.update({i['由谁创建']: num})

    # 待验证BUG数
    # print('———————————————————— 待验证BUG数 ————————————————————')
    for i in tester_list3:
        num = getdateNum(my_datas, i)
        # print("{} 待验证BUG数为：{}".format(i['指派给'],num))
        tester_dict3.update({i['指派给']: num})

    x = PrettyTable(["测试人员", "今日提交BUG数", "今日验证BUG数", "待验证BUG数"])
    for i in range(len(tester)):
        list = []
        list.append(tester[i])
        list.append(tester_dict1[tester[i]])
        list.append(tester_dict2[tester[i]])
        list.append(tester_dict3[tester[i]])
        x.add_row(list)
    print(x)

    return None

def draw(list, dict):
    # 每日新增BUG数
    list = list

    dict1 = {i:getdateNum(my_datas, {"创建日期": i}) for i in list}
    draw_chart(dict1, 'bugs', 'bug_datas', '每日新增bug数', './img/每日新增bug数.jpg')

    # 每日待修复BUG数
    dict2 = dict
    draw_chart(dict2, 'bugs', 'bug_datas', '每日待修复BUG数', './img/每日待修复BUG数.jpg')

    # 每日已解决BUG数
    dict3 = {i: getdateNum(my_datas, {"解决日期": i}) for i in list}
    draw_chart(dict3, 'bugs', 'bug_datas', '每日解决bug数', './img/每日解决bug数.jpg')

    # 每日关闭BUG数
    dict4 = {i: getdateNum(my_datas, {"关闭日期": i}) for i in list}
    draw_chart(dict4, 'bugs', 'bug_datas', '每日关闭bug数', './img/每日关闭bug数.jpg')


if __name__ == '__main__':
    today = strftime("%Y-%m-%d", localtime(time()))
    #
    # # 获取数据文件
    my_datas = getDatas('data.csv')
    print(my_datas)

    # # 初始化开发测试人员
    # # developer = ['褚亚良', '张夏泉', '李星', '沈滔', '尹君', '黄晨', '袁章珂', '温鑫', '边家家', '龙庆玉', '龚树理', '徐益森', '曾俊', '李雄', '王佳乐', '秦真',
    # #              '饶滔', '吴吉', '罗沙', '毛志敏', '谭啸', '贺尹红', '陈金强']
    # developer = ["马颖嘉", "蔡义逢", "赵涛涛", "龚树理", "张琦", "李坚", "荆斌", "池宇", "王盼"]
    # # tester = ['袁妙妙', '贾真', '潘静', '苏林子', '伍洋', '朱双平', '罗闪', '黄超', '王庆宁', '冷梅']
    # tester = ["王庆宁", "袁妙妙", "贾真", "潘静", "黄超", "苏林子"]
    #
    # # 统计开发/测试详细数据
    # statisticsData(my_datas,developer,tester,today)
    #
    # # 统计总数居 -> 返回当日激活BUG数
    # activation_bugs = statisticsDta(my_datas,today)
    #
    # # 画图表
    # list = ["2020-11-23", today]
    # dict = {"2020-11-23":69, today:activation_bugs}
    # draw(list, dict)




import csv
import time
import datetime


def test(d):
    dict = d
    dict_len = len(dict)
    key = [key for key in dict.keys()]
    value = [value for value in dict.values()]
    result = []

    with open ('data.csv', newline='', encoding="UTF-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        my_data = [data for data in spamreader]

    for list in my_data:
        for i in range(dict_len):
            if list[key[i]] != value[i]:
                break
            if i == dict_len-1 and list[key[i]] == value[i]:
                result.append(list)
    result_len = len(result)
    return result_len

if __name__ == '__main__':
    # d = {22: '孙阳'}
    # print(test(d))

# Bug编号 : 0
# 所属产品 : 1
# 所属模块 : 2
# 所属项目 : 3
# 相关需求 : 4
# 相关任务 : 5
# Bug标题 : 6
# 关键词 : 7
# 严重程度 : 8
# 优先级 : 9
# Bug类型 : 10
# 操作系统 : 11
# 浏览器 : 12
# 重现步骤 : 13
# Bug状态 : 14
# 截止日期 : 15
# 激活次数 : 16
# 是否确认 : 17
# 抄送给 : 18
# 由谁创建 : 19
# 创建日期 : 20
# 影响版本 : 21
# 指派给 : 22
# 指派日期 : 23
# 解决者 : 24
# 解决方案 : 25
# 解决版本 : 26
# 解决日期 : 27
# 由谁关闭 : 28
# 关闭日期 : 29
# 重复ID : 30
# 相关Bug : 31
# 相关用例 : 32
# 最后修改者 : 33
# 修改日期 : 34
# 附件 : 35

    # print(time.ctime())
    # print(time.time())
    # print(time.localtime(time.time()))
    # print(time.strftime("%Y-%m-%d", time.localtime(time.time())))

    a = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


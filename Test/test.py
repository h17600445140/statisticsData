import csv

# n = 0
# create_time = 20

# 获取数据
def getDatas(path):
    with open (path, newline='', encoding="UTF-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        my_datas = [data for data in spamreader]
    return my_datas

my_datas = getDatas('data.csv')

print(my_datas[0].index("严重程度"))

print(my_datas[0].index("创建日期"))

def getdateNum(condition) -> int:
    index = my_datas[0].index(condition)
    count = 0
    for i in range(1, len(my_datas)):
        if my_datas[i][index] == "2020-11-13":
            count = count + 1
    return count

print(getdateNum("创建日期"))










# for list in my_data:
#     for i in range(dict_len):
#         if list[key[i]] != value[i]:
#             break
#         if i == dict_len - 1 and list[key[i]] == value[i]:
#             result.append(list)
# result_len = len(result)

# for index in range(len(my_data[0])):
#     print("{} : {}".format(my_data[0][index], index),end=' , ')
#
# for i in range(1,len(my_data)):
#     print(my_data[i])





    # print(type(spamreader))
    # print(spamreader.line_num)
    # for row in spamreader:
    #     # row为list对象
    #     # if row[20] == '2020-10-20':
    #     if row[19] == '张锐':
    #         n+=1
    #         print(row)
    # print(n)

# if __name__ == '__main__':
#     pass

import csv

# n = 0

# create_time = 20

with open ('data.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    my_data = [data for data in spamreader]


    for index in range(len(my_data[0])):
        print("{} : {}".format(my_data[0][index], index))

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

# a = [1,2,3]
# b = [4,5,6]
# for j in b:
#     print(j)
#     for i in a:
#         if i == 2:
#             break
#         print(i)
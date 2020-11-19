import csv


with open('data2.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    my_data = [data for data in spamreader]

with open('data1.csv', newline='', encoding="UTF-8") as csvfile1:
    spamreader = csv.reader(csvfile1, delimiter=',', quotechar='"')
    my_data1 = [data for data in spamreader]


with open("data3.csv", 'w', newline='', encoding="UTF-8") as csvfile2:
    writer = csv.writer(csvfile2)
    writer.writerows(my_data)
    writer.writerows(my_data1)


with open('data3.csv', newline='', encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    my_datas = [data for data in spamreader]

print(len(my_datas))



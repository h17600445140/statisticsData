import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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
    y = np.arange(0, num, 5)

    # fig：
    # ax：图表内容对象
    fig, ax = plt.subplots()

    # width：柱状图的宽度
    bar_width = 0.5
    # 画柱状图
    Bar_chart = ax.bar(x, bugs_data, bar_width, label=label_name, color='#87CEFA')

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
    # 保存图片
    plt.savefig(path)   # 'img/test.jpg'
    plt.show()

if __name__ == '__main__':
    dict = {"2020-10-13":20, "2020-10-14":34, "2020-10-15":30, "2020-10-16":35, "2020-10-19":27}
    draw_chart(dict, 'bugs', 'bug_datas', '每日新增bug数', './img/test1.jpg')

    # print(dict.values())
    #
    # for key,value in dict.items():
    #     print(type(key),type(value))
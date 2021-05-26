# -*- coding: utf-8 -*-
import base64

class Man(object):

    # @property 装饰的对象函数是一个getter函数，一般用来获取某些数据，不会向函数中传递参数 对象.函数名
    @property
    def work(self):
        print('执行了@prperty装饰的work对象函数')
        return 123

    # @work.setter 装饰的函数，可以向该函数中传递参数，对象.函数名 = 参数值,一般用来设置某些数据
    @work.setter
    def work(self, value):
        # 具体功能代码
        print('传递进来的数据为：%s'%value)



if __name__ == '__main__':
    m = Man()
    # print(m.work)
    m.work = 2

    print(base64.b64encode("hello".encode('utf-8')))



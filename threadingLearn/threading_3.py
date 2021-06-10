# -*- coding:utf-8 -*-

import threading
import time

num = 100

def worker1():
    global num
    for i in range(3):
        num += 1
        print('worker1子线程，num：%d'%num)

def worker2():

    print('worker2子线程，num：%d'%num)


if __name__ == '__main__':
    start_time = time.time()

    print('主线程，num：%d'%num)

    t1 = threading.Thread(target=worker1)
    t1.start()

    t2 = threading.Thread(target=worker2)
    t2.start()

    print('主线程，num：%d' % num)

    end_time = time.time()
    # print('总共执行时间为%s' % (end_time - start_time))
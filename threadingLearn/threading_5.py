# -*- coding:utf-8 -*-

# 线程锁1

import threading
import time

g_num = 0

def worker():

    global g_num

    for i in range(1000000):
        flag = mutex.acquire(True)
        if flag:
            g_num += 1
            mutex.release()

if __name__ == '__main__':
    # start_time = time.time()

    mutex = threading.Lock()
    threadList = []
    for i in range(2):
        t = threading.Thread(target=worker)
        t.start()
        threadList.append(t)

    for t in threadList:
        t.join()

    print('主线程，num：%d' % g_num)

    # end_time = time.time()
    # print('总共执行时间为%s' % (end_time - start_time))
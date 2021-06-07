# -*- coding:utf-8 -*-

import threading
import time

def run():
    print(" hello world !")
    time.sleep(1)

if __name__ == '__main__':
    start_time = time.time()

    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        print(len(threading.enumerate()))   # 查看当前线程数量

    end_time = time.time()
    print('总共执行时间为%s' % (end_time - start_time))
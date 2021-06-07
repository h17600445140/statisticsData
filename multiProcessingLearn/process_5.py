# -*- coding:utf-8 -*-

from multiprocessing import Process
import time

def run():
    print(" hello world !")
    time.sleep(1)

if __name__ == '__main__':
    start_time = time.time()

    pool = []
    for i in range(5):
        p = Process(target=run)
        p.start()
        pool.append(p)

    for p in pool:
        p.join()

    end_time = time.time()
    print('总共执行时间为%s' % (end_time - start_time))
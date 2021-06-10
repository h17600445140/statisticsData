# -*- coding:utf-8 -*-

# 锁的先后顺序

import threading
import time

def a():
    mutex.acquire()
    for i in range(3):
        print('i 值为 %d'%i)
        time.sleep(1)
    mutex.release()


def b():
    mutex.acquire()
    for j in range(3):
        print('j 值为 %d'%j)
        time.sleep(1)
    mutex.release()


if __name__ == '__main__':

    mutex = threading.Lock()

    t1 = threading.Thread(target=a)
    t1.start()
    t2 = threading.Thread(target=b)
    t2.start()

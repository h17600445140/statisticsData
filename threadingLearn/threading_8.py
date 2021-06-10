# -*- coding:utf-8 -*-

# 死锁

import threading
import time



class MyThreadOne(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        if mutexA.acquire():
            print(self.name + ' ----- do1 -----up----- ')
            time.sleep(1)
            if mutexB.acquire():
                print(self.name + ' ----- do1 -----down----- ')
                mutexB.release()
            mutexA.release()


class MyThreadTwo(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        if mutexB.acquire():
            print(self.name + ' ----- do2 -----up----- ')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name + ' ----- do2 -----down----- ')
                mutexA.release()
            mutexB.release()


if __name__ == '__main__':

    mutexA = threading.Lock()
    mutexB = threading.Lock()

    t1 = MyThreadOne()
    t2 = MyThreadTwo()

    t1.start()
    t2.start()

# -*- coding:utf-8 -*-

import threading
import time

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'I am ' + self.name + ' @ ' +str(i)
            print(msg)


if __name__ == '__main__':
    start_time = time.time()

    for i in range(5):
        t = MyThread()
        t.start()

    end_time = time.time()
    print('总共执行时间为%s' % (end_time - start_time))
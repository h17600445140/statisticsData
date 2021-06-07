# -*- coding:utf-8 -*-

# 继承Process，重写run方法

from multiprocessing import Process
import os
import time

# 定义自己的进程类
class MyProcess(Process):

    def __init__(self, interval):
        Process.__init__(self)
        # super(MyProcess, self).__init__()
        self.interval = interval

    def run(self):
        print('子进程开始执行，子进程为：%s，父进程为：%s'%(os.getpid(), os.getppid()))
        t1 = time.time()
        time.sleep(self.interval)
        t2 = time.time()
        print('执行时间为%s'%(t2-t1))

if __name__ == '__main__':
    start_time = time.time()

    p = MyProcess(2)
    p.start()
    p.join()

    end_time = time.time()
    print('全部进程执行时间为%s' % (end_time - start_time))
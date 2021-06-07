# -*- coding:utf-8 -*-

# Process(target[,name[,args[,[kwargs]]]])
# function: is_alive() terminate() run()
# 属性：name pid

from multiprocessing import Process
import os

def run_proc(name):
    print("子进程运行中，name=%s，pid=%d，ppid=%d"%(name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print("父进程：%d..."%os.getpid())

    p = Process(target=run_proc, args=('hc',))
    print("子进程执行")
    p.start()   # 启动进程
    p.join()    # 父进程等待子进程
    print("子进程执行结束")


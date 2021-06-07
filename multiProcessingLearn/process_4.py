# -*- coding:utf-8 -*-

# 进程池

from multiprocessing import Pool
import os
import time



def run(num):
    print('子进程开始执行，子进程为：%s，父进程为：%s'%(os.getpid(), os.getppid()))
    t1 = time.time()
    print(num)
    time.sleep(2)
    t2 = time.time()
    print('子进程执行时间为%s'%(t2-t1))

if __name__ == '__main__':
    start_time = time.time()

    # 创建进程池
    pool = Pool(3)

    for num in range(10):
        # pool.apply_async(run, args=(num,))
        pool.apply(run, args=(num,))

    # 关闭进程池
    pool.close()
    # 父进程等待进程池的结束
    pool.join()

    end_time = time.time()
    print('全部进程总共执行时间为%s' % (end_time - start_time))
# -*- coding:utf-8 -*-

# 线程锁3

import threading

num = 0

def add():
    lock.acquire()  # 上锁
    global num
    for i in range(10000000):  # 一千万次
        num += 1
    lock.release()  # 解锁

def sub():
    lock.acquire()  # 上锁
    global num
    for i in range(10000000):  # 一千万次
        num -= 1
    lock.release()  # 解锁

if __name__ == '__main__':
    lock = threading.Lock()  # 实例化同步锁对象

    t1 = threading.Thread(target=add, )
    t2 = threading.Thread(target=sub, )
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("最终结果:", num)
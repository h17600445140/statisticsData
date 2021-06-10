# -*- coding:utf-8 -*-

# 线程锁2

import threading

num = 0
def add():
    global num
    for i in range(10000000):  # 一千万次
        num += 1

def sub():
    global num
    for i in range(10000000):  # 一千万次
        num -= 1

if __name__ == '__main__':


    t1 = threading.Thread(target=add,)
    t2 = threading.Thread(target=sub,)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("最终结果:",num)
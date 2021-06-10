# -*- coding:utf-8 -*-

# ThreadLocal 变量（每个线程只能使用自己线程的独立副本，各不相扰）

import threading

local_school = threading.local()

def process_student():

    student = local_school.student
    print('Hello, %s in %s'%(student, threading.current_thread().name))

def process_thread(name):

    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('黄同学',), name='t1')
t2 = threading.Thread(target=process_thread, args=('超同学',), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()